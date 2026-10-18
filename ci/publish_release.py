"""Publish an owner-signed installer. This repository contains no app source or private key."""
import base64
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

REPO = 'dtcnexis/DTC-Nexis-Updates'
MAX_ARCHIVE = 260 * 1024 * 1024


def gh(*args, data=None, check=True):
    return subprocess.run(['gh', *args], input=None if data is None else json.dumps(data),
                          text=True, capture_output=True, check=check)


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as file:
        for block in iter(lambda: file.read(1024*1024), b''):
            h.update(block)
    return h.hexdigest()


def require_owner_release_approval(revision):
    """Block all publishing unless owner explicitly approves this exact revision.

    A valid code-signing cert without an approved pinned signer is insufficient.
    This helper performs no network, release, installation, or GitHub actions.
    """
    if os.environ.get('NEXIS_OWNER_APPROVED_REVISION') != str(revision):
        raise RuntimeError('BLOCK RELEASE: owner has not approved this exact revision')
    approved_thumbprint = os.environ.get('NEXIS_APPROVED_SIGNER_THUMBPRINT', '').strip()
    approved_file_version = os.environ.get('NEXIS_APPROVED_WINDOWS_FILE_VERSION', '').strip()
    if not re.fullmatch(r'[0-9a-fA-F]{40}', approved_thumbprint):
        raise RuntimeError('BLOCK RELEASE: expected owner-approved publisher signer fingerprint is not configured')
    if not re.fullmatch(r'\d+\.\d+\.\d+(?:\.\d+)?', approved_file_version):
        raise RuntimeError('BLOCK RELEASE: owner-approved Windows FileVersion is not configured')
    if not any(int(x) for x in approved_file_version.split('.')):
        raise RuntimeError('BLOCK RELEASE: owner-approved Windows FileVersion must not be all zero')
    return approved_thumbprint, approved_file_version


def main():
    assert os.environ.get('GITHUB_REPOSITORY') == REPO
    request = json.loads(Path('release-request.json').read_text())
    verified = subprocess.run(['node','ci/verify-feed.cjs','pending-update-feed.json','update-public-key.json'],
                              text=True,capture_output=True,check=True)
    release = json.loads(verified.stdout)
    revision = release['versionCode']
    # Fail closed before any release lookup, upload, or feed modification.
    approved_thumbprint, approved_file_version = require_owner_release_approval(revision)
    asset = f'DTC_NEXIS_SETUP_R{revision}.exe'
    assert request['revision'] == revision
    assert set(request) == {'revision', 'installer_sha256', 'parts'}
    assert request['installer_sha256'] == release['windows']['sha256']
    assert isinstance(request['parts'], list) and 1 <= len(request['parts']) <= 100
    with tempfile.TemporaryDirectory() as folder:
        temp = Path(folder)
        installer = temp/asset
        total = 0
        with installer.open('wb') as output:
            for index, part in enumerate(request['parts'], 1):
                assert part['path'] == f'installer-parts/v{revision}/part-{index:02}.bin'
                file = Path(part['path'])
                assert file.is_file() and not file.is_symlink()
                assert file.stat().st_size == part['size'] and digest(file) == part['sha256']
                total += part['size']
                assert total <= MAX_ARCHIVE, 'Installer too large'
                output.write(file.read_bytes())
        assert total >= 1024
        assert digest(installer) == release['windows']['sha256'], 'Installer signature manifest checksum differs'
        with installer.open('rb') as file:
            assert file.read(2) == b'MZ', 'Not a Windows executable'
        # Fail closed: a signed feed and matching SHA-256 do not prove that
        # Windows trusts the installer. Verify the FINAL bytes before publishing
        # the release or updating the public feed.
        if os.name != 'nt':
            raise RuntimeError('BLOCK RELEASE: Windows Authenticode verification requires a Windows runner')
        subprocess.run(
            ['pwsh', '-NoProfile', '-NonInteractive', '-File',
             'ci/verify-windows-installer-signature.ps1', '-Installer', str(installer),
             '-ExpectedPublisherThumbprint', approved_thumbprint,
             '-ExpectedFileVersion', approved_file_version],
            check=True,
        )
        tag = f'v{revision}'
        existing = gh('release','view',tag,'--repo',REPO,'--json','tagName',check=False)
        if existing.returncode == 0:
            previous = temp/'existing';previous.mkdir()
            gh('release','download',tag,'--repo',REPO,'--pattern',asset,'--dir',str(previous))
            assert digest(previous/asset) == release['windows']['sha256'], 'An immutable release cannot be replaced'
        else:
            gh('release','create',tag,str(installer),'--repo',REPO,'--prerelease',
               '--title',f'DTC NEXIS Windows public test — revision {revision}',
               '--notes-file','RELEASE_NOTES.md')

    # Only make the channel live after the permanent installer exists.
    current = gh('api',f'repos/{REPO}/contents/update-feed.json',check=False)
    previous_sha = None
    if current.returncode == 0:
        current = json.loads(current.stdout)
        old_envelope = json.loads(base64.b64decode(current['content']))
        old = json.loads(base64.b64decode(old_envelope['payload']))
        assert old['versionCode'] <= revision, 'Refusing to roll back the public channel'
        if old['versionCode'] == revision:
            assert old == release, 'An existing revision must identify the same installer'
        previous_sha = current['sha']
    data = {'message':f'Publish signed Windows update revision {revision}',
            'content':base64.b64encode(Path('pending-update-feed.json').read_bytes()).decode(),
            'branch':'main'}
    if previous_sha:
        data['sha'] = previous_sha
    gh('api','--method','PUT',f'repos/{REPO}/contents/update-feed.json','--input','-',data=data)
    print('PASS: immutable installer published and signed public update channel activated')


if __name__ == '__main__':
    main()

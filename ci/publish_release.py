"""Publish an owner-signed installer. This repository contains no app source or private key."""
import base64
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import urllib.request
from urllib.parse import urlsplit
import zipfile

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


class HTTPSOnly(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, url):
        if urlsplit(url).scheme != 'https':
            raise ValueError('Archive redirect must use HTTPS')
        return super().redirect_request(req, fp, code, msg, headers, url)


def main():
    assert os.environ.get('GITHUB_REPOSITORY') == REPO
    request = json.loads(Path('release-request.json').read_text())
    verified = subprocess.run(['node','ci/verify-feed.cjs','pending-update-feed.json','update-public-key.json'],
                              text=True,capture_output=True,check=True)
    release = json.loads(verified.stdout)
    revision = release['versionCode']
    asset = f'DTC_NEXIS_SETUP_R{revision}.exe'
    assert request['revision'] == revision
    assert re.fullmatch(r'[a-f0-9]{64}', request['archive_sha256'])
    source = urlsplit(request['archive_url'])
    assert source.scheme == 'https' and source.hostname and not source.username and not source.password
    assert request['archive_member'] == 'DTC_NEXIS_PUBLIC_CHANNEL_TEST.exe'
    with tempfile.TemporaryDirectory() as folder:
        temp = Path(folder)
        archive = temp/'installer.zip'
        try:
            opener = urllib.request.build_opener(HTTPSOnly())
            with opener.open(request['archive_url'],timeout=90) as response, archive.open('wb') as output:
                total = 0
                while chunk := response.read(1024*1024):
                    total += len(chunk)
                    assert total <= MAX_ARCHIVE, 'Installer archive too large'
                    output.write(chunk)
        except Exception:
            raise SystemExit('Installer transfer expired or failed. Refresh the installer-only transfer link.') from None
        assert digest(archive) == request['archive_sha256'], 'Installer archive checksum differs'
        installer = temp/asset
        with zipfile.ZipFile(archive) as package:
            members = [item for item in package.infolist() if not item.is_dir()]
            assert len(members) == 1 and members[0].filename == request['archive_member'], 'Expected an installer-only archive'
            assert 1024 <= members[0].file_size <= MAX_ARCHIVE
            with package.open(members[0]) as source_file, installer.open('wb') as output:
                while chunk := source_file.read(1024*1024):
                    output.write(chunk)
        assert digest(installer) == release['windows']['sha256'], 'Installer signature manifest checksum differs'
        with installer.open('rb') as file:
            assert file.read(2) == b'MZ', 'Not a Windows executable'
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

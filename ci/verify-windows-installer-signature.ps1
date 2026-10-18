# DTC NEXIS public publisher (DRAFT ONLY). Never publish without owner approval.
param(
    [Parameter(Mandatory=$true)][string]$Installer,
    [Parameter(Mandatory=$true)][string]$ExpectedPublisherThumbprint,
    [Parameter(Mandatory=$true)][string]$ExpectedFileVersion
)
$ErrorActionPreference='Stop'
if (!(Test-Path -LiteralPath $Installer -PathType Leaf)) {
    throw 'BLOCK RELEASE: installer missing'
}
$sig=Get-AuthenticodeSignature -LiteralPath $Installer
if ($sig.Status -ne 'Valid') {
    throw "BLOCK RELEASE: Authenticode status is $($sig.Status). A signed update feed does NOT sign an EXE."
}
if (!$sig.SignerCertificate) { throw 'BLOCK RELEASE: no signer certificate' }
if (!$sig.TimeStamperCertificate) { throw 'BLOCK RELEASE: no trusted timestamp' }
# Only the owner-approved certificate is acceptable, not any valid publisher.
if ($ExpectedPublisherThumbprint -notmatch '^[0-9a-fA-F]{40}$') {
    throw 'BLOCK RELEASE: approved publisher certificate thumbprint missing'
}
$cert=$sig.SignerCertificate
$actual=([string]$cert.Thumbprint).Replace(' ','').ToUpperInvariant()
if ($actual -ne $ExpectedPublisherThumbprint.ToUpperInvariant()) {
    throw 'BLOCK RELEASE: signer does not match owner-approved certificate'
}
if ($ExpectedFileVersion -notmatch '^\d+\.\d+\.\d+(\.\d+)?$') {
    throw 'BLOCK RELEASE: approved Windows FileVersion missing'
}
$expected=[version]$ExpectedFileVersion
if ($expected -le [version]'0.0.0.0') { throw 'BLOCK RELEASE: invalid zero version' }
$version=([string](Get-Item -LiteralPath $Installer).VersionInfo.FileVersion).Trim()
if ($version -notmatch '^\d+\.\d+\.\d+(\.\d+)?$') {
    throw 'BLOCK RELEASE: invalid numeric Windows FileVersion'
}
if ([version]$version -ne $expected) {
    throw 'BLOCK RELEASE: Windows FileVersion does not match owner-approved version'
}
Write-Host 'PASS: approved Windows Authenticode signer, timestamp and exact version verified'
Write-Host "FileVersion: $version"
Write-Host "SHA256: $((Get-FileHash -LiteralPath $Installer -Algorithm SHA256).Hash)"
# Valid signing does not guarantee Microsoft Smart App Control approval.

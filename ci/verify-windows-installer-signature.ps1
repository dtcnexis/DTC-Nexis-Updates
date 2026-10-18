# R7 Windows installer signing gate (PowerShell)
# Run on Windows CI after building/signing and before release upload.
param(
    [Parameter(Mandatory=$true)][string]$Installer,
    [Parameter(Mandatory=$true)][string]$ExpectedPublisherThumbprint,
    [Parameter(Mandatory=$true)][string]$ExpectedFileVersion
)
$ErrorActionPreference = 'Stop'
if (!(Test-Path -LiteralPath $Installer -PathType Leaf)) { throw "Installer missing: $Installer" }
$sig = Get-AuthenticodeSignature -LiteralPath $Installer
if ($sig.Status -ne 'Valid') { throw "BLOCK RELEASE: Authenticode status is $($sig.Status). A signed update-feed.json does NOT sign the EXE." }
if (!$sig.SignerCertificate) { throw 'BLOCK RELEASE: no signer certificate' }
$cert = $sig.SignerCertificate
if ($cert.NotAfter -lt (Get-Date)) { throw 'BLOCK RELEASE: signer certificate expired' }
if (!$sig.TimeStamperCertificate) { throw 'BLOCK RELEASE: no trusted timestamp found' }
# Never trust an arbitrary code-signing certificate. The approved fingerprint
# must come from the owner's protected release configuration.
if ($ExpectedPublisherThumbprint -notmatch '^[0-9a-fA-F]{40}
$version = (Get-Item -LiteralPath $Installer).VersionInfo
if (!$version.FileVersion -or $version.FileVersion -notmatch '^\d+\.\d+\.\d+(\.\d+)?
Write-Host "PASS: valid Authenticode signature, timestamp, owner-pinned signer, and exact FileVersion"
Write-Host "Signer: $($cert.Subject)"
Write-Host "FileVersion: $($version.FileVersion)"
Write-Host "SHA256: $((Get-FileHash -LiteralPath $Installer -Algorithm SHA256).Hash)"
# This gate does not guarantee Smart App Control reputation or approval.
) {
  throw 'BLOCK RELEASE: owner-approved signer fingerprint not configured'
}
$actual = ([string]$cert.Thumbprint).Replace(' ','').ToUpperInvariant()
if ($actual -ne $ExpectedPublisherThumbprint.ToUpperInvariant()) {
  throw 'BLOCK RELEASE: signed by a different publisher certificate'
}
if ($ExpectedFileVersion -notmatch '^\d+\.\d+\.\d+(\.\d+)?
$version = (Get-Item -LiteralPath $Installer).VersionInfo
if (!$version.FileVersion -or $version.FileVersion -eq '0.0.0.0') { throw 'BLOCK RELEASE: invalid FileVersion' }
Write-Host "PASS: valid Authenticode signature and timestamp"
Write-Host "Signer: $($cert.Subject)"
Write-Host "FileVersion: $($version.FileVersion)"
Write-Host "SHA256: $((Get-FileHash -LiteralPath $Installer -Algorithm SHA256).Hash)"
# This gate does not guarantee Smart App Control reputation or approval.
 -or [version]$ExpectedFileVersion -le [version]'0.0.0.0') {
  throw 'BLOCK RELEASE: invalid approved FileVersion configuration'
}
$version = (Get-Item -LiteralPath $Installer).VersionInfo
if (!$version.FileVersion -or $version.FileVersion -eq '0.0.0.0') { throw 'BLOCK RELEASE: invalid FileVersion' }
Write-Host "PASS: valid Authenticode signature and timestamp"
Write-Host "Signer: $($cert.Subject)"
Write-Host "FileVersion: $($version.FileVersion)"
Write-Host "SHA256: $((Get-FileHash -LiteralPath $Installer -Algorithm SHA256).Hash)"
# This gate does not guarantee Smart App Control reputation or approval.
 -or [version]$version.FileVersion -ne [version]$ExpectedFileVersion) {
  throw 'BLOCK RELEASE: Windows FileVersion differs from owner-approved release version'
}
Write-Host "PASS: valid Authenticode signature and timestamp"
Write-Host "Signer: $($cert.Subject)"
Write-Host "FileVersion: $($version.FileVersion)"
Write-Host "SHA256: $((Get-FileHash -LiteralPath $Installer -Algorithm SHA256).Hash)"
# This gate does not guarantee Smart App Control reputation or approval.
) {
  throw 'BLOCK RELEASE: owner-approved signer fingerprint not configured'
}
$actual = ([string]$cert.Thumbprint).Replace(' ','').ToUpperInvariant()
if ($actual -ne $ExpectedPublisherThumbprint.ToUpperInvariant()) {
  throw 'BLOCK RELEASE: signed by a different publisher certificate'
}
if ($ExpectedFileVersion -notmatch '^\d+\.\d+\.\d+(\.\d+)?
$version = (Get-Item -LiteralPath $Installer).VersionInfo
if (!$version.FileVersion -or $version.FileVersion -eq '0.0.0.0') { throw 'BLOCK RELEASE: invalid FileVersion' }
Write-Host "PASS: valid Authenticode signature and timestamp"
Write-Host "Signer: $($cert.Subject)"
Write-Host "FileVersion: $($version.FileVersion)"
Write-Host "SHA256: $((Get-FileHash -LiteralPath $Installer -Algorithm SHA256).Hash)"
# This gate does not guarantee Smart App Control reputation or approval.
 -or [version]$ExpectedFileVersion -le [version]'0.0.0.0') {
  throw 'BLOCK RELEASE: invalid approved FileVersion configuration'
}
$version = (Get-Item -LiteralPath $Installer).VersionInfo
if (!$version.FileVersion -or $version.FileVersion -eq '0.0.0.0') { throw 'BLOCK RELEASE: invalid FileVersion' }
Write-Host "PASS: valid Authenticode signature and timestamp"
Write-Host "Signer: $($cert.Subject)"
Write-Host "FileVersion: $($version.FileVersion)"
Write-Host "SHA256: $((Get-FileHash -LiteralPath $Installer -Algorithm SHA256).Hash)"
# This gate does not guarantee Smart App Control reputation or approval.

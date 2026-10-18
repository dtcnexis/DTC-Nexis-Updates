# R7 Windows installer signing gate (PowerShell)
# Run on Windows CI after building/signing and before release upload.
param([Parameter(Mandatory=$true)][string]$Installer)
$ErrorActionPreference = 'Stop'
if (!(Test-Path -LiteralPath $Installer -PathType Leaf)) { throw "Installer missing: $Installer" }
$sig = Get-AuthenticodeSignature -LiteralPath $Installer
if ($sig.Status -ne 'Valid') { throw "BLOCK RELEASE: Authenticode status is $($sig.Status). A signed update-feed.json does NOT sign the EXE." }
if (!$sig.SignerCertificate) { throw 'BLOCK RELEASE: no signer certificate' }
$cert = $sig.SignerCertificate
if ($cert.NotAfter -lt (Get-Date)) { throw 'BLOCK RELEASE: signer certificate expired' }
if (!$sig.TimeStamperCertificate) { throw 'BLOCK RELEASE: no trusted timestamp found' }
$version = (Get-Item -LiteralPath $Installer).VersionInfo
if (!$version.FileVersion -or $version.FileVersion -eq '0.0.0.0') { throw 'BLOCK RELEASE: invalid FileVersion' }
Write-Host "PASS: valid Authenticode signature and timestamp"
Write-Host "Signer: $($cert.Subject)"
Write-Host "FileVersion: $($version.FileVersion)"
Write-Host "SHA256: $((Get-FileHash -LiteralPath $Installer -Algorithm SHA256).Hash)"
# This gate does not guarantee Smart App Control reputation or approval.

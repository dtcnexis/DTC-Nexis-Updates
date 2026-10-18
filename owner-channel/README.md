# DTC NEXIS — permanent owner trial data feed

One persistent channel endpoint:

`https://raw.githubusercontent.com/dtcnexis/DTC-Nexis-Updates/owner-stable-data-channel/owner-channel/update-feed.json`

## Update contract

- Do not change this endpoint or the pinned P-256 signing public key between revisions.
- The current signed envelope is the **unchanged valid Revision 9** owner feed, with 18 demonstration DTCs.
- For Revision 10 and beyond, update **the contents of the same `update-feed.json`**, not the link or branch. The next feed must be signed by the previously authorized private signing key, and its data must contain cryptographic digests, version/revision guards and existing signed package references.
- Package files can be stored as immutable versioned assets under `owner-channel/packages/`; only the signed manifest points to them.
- Never place a private signing key in this repository or installer. If the key is replaced, require an explicit controlled trust migration, not a silent reset.
- Generic codes must not be mixed with manufacturer-specific definitions. Do not release PNGs without independent technical signoff.
- This branch is separate from `main`, which remains unchanged. **Do not attach this channel to publicly distributed applications**, publish a release, or deliver a dataset to other users without specific authorization.
- The repository itself can be publicly readable; a non-advertised branch is **not a confidentiality barrier**. Keep all private VINs, workshop records, licensing information, client data, and secrets out of this repository.

## Explicit current limitations
- This channel presently contains an existing signed Revision 9; no new Revision 10 content or images have been published.
- Historical Revision 9's signed catalog URL points to an immutable older owner-trial branch, which remains readable. Future signed catalogs should be built under this permanent owner channel.
- Windows executable code changes cannot be delivered as data-only updates. Trusted Windows Authenticode signing is separately required before distribution onto a Smart App Control-protected laptop.

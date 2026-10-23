# Security Fixes

## High
- [x] Remove the hardcoded webhook in `on_connect`; never send `LICENSE_KEY`, user IDs, or machine stats (opt-in only)
- [x] Remove the `cordauth.onrender.com` startup gate, or make it optional and non-blocking
- [x] Delete the `os.system(f"start {download_link}")` auto-update in KeyAuth `init`; use a signed/manual update instead
- [x] Stop sending `prvtkey` to `api.tatum.io`; use a Tatum KMS signature ID or sign locally, and drop `prvtkey` from `ltc.yaml`

## Medium
- [ ] Keep secrets out of plaintext files: load token/license/key from env or OS keyring, `chmod 600` config files, add them to `.gitignore`
- [ ] Pin every dependency in `infreq.txt` (currently only `discord.py-self` is pinned)
- [ ] Require confirmation or a feature flag for destructive commands (`nuke`, `massban`, `massdm`, `spam`)

## Low
- [ ] Validate/sanitize URLs passed to `screenshot`, `servericon`, and webhook settings
- [ ] Sign the release binary and publish a SHA-256 so builds can be verified

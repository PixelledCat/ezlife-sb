# EzLife x2 Official Version

Thank you for choosing EzLife x2 Official Version! The only premium selfbot in this scene.

EzLife is a Discord selfbot built on `discord.py-self`. It runs on your own user token and only responds to commands sent by the account configured in `config.ini`.

## Requirements

- Python 3.9+
- A Discord user token (your own account)
- Internet access for the crypto price and balance APIs

## Getting Started

### 1. Install dependencies

```bash
pip install -r infreq.txt
```

Using a virtual environment is recommended:

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r infreq.txt
```

### 2. Configure `config.ini`

If `config.ini` does not exist, it is created automatically on first run. Fill in your details:

```ini
[EzLife]
token = (Your selfbot token)
userid = (Your user ID)
prefix = .                       ; command prefix; leave empty for no prefix

[DeleteMsgWebhook]
deleted_logs = False             ; True/False - log deleted messages
deletemsgwebhookurl =

[SniperWebhook]
sniperwebhookurl =               ; webhook for nitro sniper hits

[CryptoWebhook]
cryptowebhookurl =               ; webhook for LTC transaction updates

[Misc]
webhookurl =
```

| Key | Description |
| --- | --- |
| `token` | Your Discord user token |
| `userid` | Your Discord user ID; only this account can run commands |
| `prefix` | Command prefix (e.g. `.`) |
| `deleted_logs` | Enable/disable deleted message logging |
| `deletemsgwebhookurl` | Webhook that receives deleted messages |
| `sniperwebhookurl` | Webhook that receives nitro sniper hits |
| `cryptowebhookurl` | Webhook that receives LTC transaction updates |

### 3. Optional configuration

- **`config.json`** - ping notification settings (`enabled`, `ping_webhook_url`). Managed by `.togglepings`.
- **`ltc.yaml`** - Tatum API credentials used by `.payltc`:

  ```yaml
  apikey: ""
  address: ""
  signatureid: ""
  ```

  The `signatureid` is required; private keys are never stored or sent.

## Usage

Start the selfbot:

```bash
python EzLife.py
```

On connect it prints your username, guild count, and total members. Use `help` to list modules and `.help <module>` to list that module's commands.

### Data files

These are created automatically as needed and persist your settings between runs:

| File | Purpose |
| --- | --- |
| `config.ini` | Bot and webhook configuration |
| `config.json` | Ping notification settings |
| `ltc.yaml` | Tatum API credentials |
| `crypto_addresses.json` | Saved crypto address book |
| `afk_data.json` | AFK status |
| `auto_messages.json` | Scheduled auto messages |
| `auto_responses.json` | Auto-response triggers |
| `subscribe.json` | LTC address subscriptions |

## Modules

| Module | Commands |
| --- | --- |
| AFK | `.afk [reason]`, `.unafk` |
| ARs | `.addar`, `.removear`, `.listar` |
| Admin | `.kick`, `.ban`, `.softban`, `.unban`, `.mute`, `.nuke`, `.massban`, `.massunban`, `.forcenick`, `.stopforcenick`, `.savebans`, `.exportbans`, `.servername`, `.servericon` |
| Automsg | `.startauto`, `.listauto`, `.stopauto`, `.deleteallauto` |
| Crypto | `.price`, `.convert`, `.getbal`, `.getbtcbal`, `.getethbal`, `.getsolbal`, `.getusdcbal`, `.getusdtbal`, `.payltc`, `.ltcsubscribe` |
| Dump | `.alldump`, `.imgdump`, `.audiodump`, `.videodump`, `.textdump`, `.emojidump`, `.emojidownload`, `.avatardump`, `.channeldump` |
| Fun | `.asci`, `.mock`, `.mockstop`, `.infect`, `.fakenitro`, `.cum` |
| Info | `.userinfo`, `.whois`, `.avatar`, `.id`, `.tokeninfo`, `.iplook`, `.stats`, `.ping` |
| Logs | Deleted message logging via webhook |
| Nsfw | `.nrandom`, `.ass`, `.boobs`, `.pussy`, `.nsfwai` |
| Pings | `.togglepings` - DM notification on mentions |
| RotateStatus | `.rotatestatus`, `.rotatestatusstart`, `.rotatestatusstop`, `.rotatestatusclear` |
| Snipe | `.snipe` |
| Sniper | `.togglesniper` - nitro gift sniper |
| Utility | `.calc`, `.nickscan`, `.adminscan`, `.scrape`, `.serverlist`, `.firstmsg`, `.nickloop`, `.stopnickname`, `.servercopy`, `.status`, `.checkpromo`, `.hypesquad`, `.screenshot`, `.search`, `.vanity`, `.massleave` |
| Vc | `.vc247`, `.vckick`, `.vcmoveall`, `.vcmute` |
| Vouch | `.createvouch`, `.v`, `.showtriggers`, `.showformat`, `.deletevouch` |
| Wizz | `.nuke`, `.nukechannels`, `.massreact`, `.spam`, `.spamgp`, `.spamdm`, `.spamrep`, `.massmention`, `.clear`, `.massdm`, `.dmannounce`, `.spamchannels`, `.dmclean`, `.randomban` |

## Crypto Address Book

Save your receiving addresses once and post them with a single command.

```
.addaddress <coin> <address>     # save an address (ltc, btc, eth, sol, usdc, usdt)
.deladdress <coin>               # remove a saved address
.addresses                       # list all saved addresses
.ltc / .btc / .eth / .sol / .usdc / .usdt    # post the saved address
```

Addresses are validated before saving and stored in `crypto_addresses.json`. `.getbal` accepts a coin name (using its saved address when omitted) or a raw address:

```
.getbal ltc            # uses the saved LTC address
.getbal btc <address>  # check a specific address
.getbal 0x...          # auto-detects ETH; use .getusdcbal/.getusdtbal for ERC-20 tokens
```

## Additional Information

- Join the official server [here](https://discord.gg/stellar-shop) for bug fixes, updates, and support
- Review the Terms of Service (TOS) provided in the AutoBuy or at https://ezlife.space/terms
- Sharing, reselling, or leaking this bot, or using it in any server that distributes pirated/leaked versions, is strictly prohibited. No support or updates will be provided in such cases.

**Security:** `config.ini`, `config.json`, `ltc.yaml`, and `crypto_addresses.json` contain secrets and are listed in `.gitignore`. Never commit or share them. A user token grants full access to the account it belongs to.

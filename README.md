# PC Hotdeal Bot (PC-parts only)

**This is a ready-to-deploy Telegram hotdeal crawler that only forwards PC component deals.**
- Includes crawlers (stubs) for: ppomppu, ruliweb, clien, quasarzone, comsclub, compuzone, coupang, gmarket, auction, 11st, naver hotdeal
- Telegram B-style detailed messages
- Dockerfile + requirements.txt
- Config example (config.yaml) — fill your TELEGRAM token & chat id before deploying

## Quick start (local)
1. Extract ZIP.
2. Create virtualenv: `python -m venv .venv && source .venv/bin/activate` (Windows: `.\.venv\Scripts\activate`)
3. Install deps: `pip install -r requirements.txt`
4. Edit `config.yaml` (put your Bot token and chat id)
5. Run: `python src/main.py`

## Quick start (Docker)
1. Build: `docker build -t pc-hotdeal-bot .`
2. Run: `docker run -d --name pc-hotdeal-bot -v $(pwd)/config.yaml:/app/config.yaml:ro pc-hotdeal-bot`

## Deploy on Railway / Render
- Push this repo to GitHub (or upload ZIP contents). Then connect to Railway and use Dockerfile or direct Python start command.

## Notes
- Crawlers are implemented as lightweight stubs that parse listing pages. Some sites may need selectors adjusted.
- Respect target sites' robots.txt and rate limits.
- No secrets are included. Add your TELEGRAM token and chat id in `config.yaml` before running.

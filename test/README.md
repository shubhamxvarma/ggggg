# EDR Developer Protection Test Repo (Dummy Secrets)

This repo contains **intentionally exposed, non-functional** secrets to help validate secret/credential detection features in EDR/DLP tools.
All keys/tokens/passwords are syntactically valid-looking but **fake**. Do not use in production.

## What’s inside
- `app.py` – trivial Flask app with inline tokens in code and comments.
- `config.py` – hard-coded dummy secrets, RSA private key string.
- `.env` – common environment-style secrets.
- `secrets.txt` – mixed bag (JWT, base64/hex-encoded values, etc.).
- `id_rsa` – dummy private key PEM (pattern only).
- `package.json` / `index.js` – JS example with embedded "secrets".

> Purpose: Trigger developer-protection/secret-scanning rules (e.g., AWS/GitHub/Stripe/Slack/Twilio/Google API keys, passwords in code, JWTs).
> All content is safe, non-sensitive, and for testing only.

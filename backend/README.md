# Backend (Django + DRF)

## Setup
1. Create and activate a virtualenv, then `pip install -r requirements.txt`
2. Create a PostgreSQL database named `kpop_ledger`
3. Copy `.env.example` to `.env` and fill in your own values
4. `python3 manage.py check`
5. `python3 manage.py runserver`, then open http://127.0.0.1:8000/api/health/

## Notes
- Do not run `migrate` until the custom User model (accounts) is finished.
- If runserver says "Dependency on app with no migrations: accounts",
  run `python3 manage.py makemigrations accounts` locally (do not commit or apply it).
- Never commit `.env`.
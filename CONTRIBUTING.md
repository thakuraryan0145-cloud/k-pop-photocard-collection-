# Repo Rules

## Branching
- `main` = production, `develop` = integration. Never push directly to either.
- Work on `feature/<short-name>`, `fix/<short-name>` or `docs/<short-name>`, branched from `develop`.
- Open a PR into `develop`; `develop` -> `main` only at milestone releases.

## Commits & PRs
- Conventional style: `feat: add collection endpoint`, `fix: ...`, `docs: ...`, `chore: ...`.
- Small PRs (<400 lines). 1 approval required; CODEOWNERS are auto-requested.
- Squash merge. Branch auto-deleted after merge.
- CI must pass (`backend-test`, `frontend-test`) before merge.

## Code
- Backend: Django migrations are source of truth; migrations must be reversible; every FK has explicit `on_delete`; every model has `created_at` / `updated_at`.
- Frontend: plain JS (no TypeScript), Tailwind tokens from Design.md.
- Tests accompany new logic.

## Secrets
- Never commit `.env`. Only `.env.example` with placeholder values.
- Real secrets live in GitHub Secrets and host env vars.

## Reviews
- Reviewers respond within 24h. Authors do not merge their own PR.

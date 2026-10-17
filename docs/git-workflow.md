# Git Workflow

## Branch Structure

Our project follows a simple Git branching workflow:

main
↓
develop
↓
feature branches

## Main Branch

The `main` branch contains the stable version of the project.

Team members should not directly push changes to the `main` branch.

## Develop Branch

The `develop` branch is used for integrating and testing the latest development work before it is merged into `main`.

## Feature Branches

Each team member should create a separate feature branch from `develop`.

Example:

feature/photocard-collection
feature/trade-ledger
feature/user-management
feature/database

## Development Workflow

1. Update the local `develop` branch.
2. Create a new feature branch from `develop`.
3. Work on the assigned feature.
4. Commit the changes.
5. Push the feature branch to GitHub.
6. Create a Pull Request.
7. Review and test the changes.
8. Merge the Pull Request into `develop`.
9. After final testing, approved changes can be merged into `main`.

## Important Rules

- Do not directly push to `main`.
- Create a separate feature branch for each feature.
- Use clear commit messages.
- Pull Requests should be reviewed before merging.
- Keep `develop` updated with the latest team changes.

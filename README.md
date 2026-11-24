# Repo Health Check

`repo-health` is a small, dependency-free CLI that checks a local repository for
basic open-source readiness: a README, license, contribution guide, code of
conduct, CI workflow, security policy, and issue templates.

It is intentionally simple so contributors can understand the code and improve
it through focused pull requests.

## Usage

```powershell
python -m repo_health . --json
```

The command exits with code `0` when all checks pass and `1` when one or more
recommended files are missing.

## Development

```powershell
python -m unittest discover -s tests -v
```

## Contribution ideas

- Add an option to treat selected checks as required.
- Add support for GitHub Actions workflow validation.
- Improve the human-readable output while preserving the JSON format.

## License

MIT

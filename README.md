# Ticket Triage

A tiny service that classifies support tickets into a category and urgency.

## How to run

First, activate the virtual environment (if one exists) so that the project's
packages are available on the Python path, e.g.:```bash
source .venv/bin/activate
```

Alternatively you can use the same interpreter for commands by prefixing with
`python -m` (this ensures the current working directory is on `sys.path`).

- Run tests:
  ```bash
  python -m pytest -q      # or PYTHONPATH=. pytest -q if you prefer
  ```

- (Optional) Run CLI: `python -m app.main --text "hello"`

To install the package editable for development:
```bash
pip install -e .
```

Known issues:
- Some tickets crash the classifier
- Output is inconsistent

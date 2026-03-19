
# Meu Projeto Seguro

Projeto mínimo em Python/Poetry para demonstrar:
- Dependency Graph do GitHub
- Dependabot (alerts e updates)
- Code Scanning (CodeQL)
- Secret Scanning (quando habilitado na organização)

## Requisitos
- Python 3.10+
- Poetry

## Como rodar localmente

```bash
poetry install
poetry run python src/app.py
poetry run pytest -q

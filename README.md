# Projet de template pour une lib python

Template pour lib python simple. Basé sur `python 3.10`

- [./src/](./src/): les sources de la bibliothèque
- [./tests](./tests/): Les tests unitaires de la bibliothèque

Les données du projet sont décrites dans [./pyproject.toml](./pyproject.toml). 

Deux ensembles de dépendances `extras` existent pour le développement locaux:
- `dev` 
- `test`

Le versionning de la bibliothèque est dynamique et dépend du tag git. Plus d'informations avec [https://https://pypi.org/project/setuptools-scm/](https://https://pypi.org/project/setuptools-scm/).

## Git hooks

La bibliothèque [https://pre-commit.com/index.html](https://pre-commit.com/index.html) est installée en dépendance de développement.

## Forge github

Le fichier [./.github/workflows/publish-test-pypi.yml](./.github/workflows/publish-test-pypi.yml) définit un *workflow github* pour la publication des tags sur la plateforme PyPI de test: [https://test.pypi.org/](https://https://test.pypi.org/)

Le script attend un secret contenant le token Test PyPI. Pour cela, renseignez un secret `TESTPYPI_TOKEN` avec le token correspondant, depuis la page de repo github, dans: `settings > secrets and variables > actions > New repository secret`

## Forge gitlab

Le fichier [./.gitlab-ci.yml](./.gitlab-ci.yml) définit une pipeline gitlab par défaut.

Le job `🧪 test` lance les tests via `pytest`
Le job `🐣 deploy` construit et déploie la bibliothèque, elle utilise des variables pour déterminer oú déployer la bibliothèque et les informations d'authentification:

- `PYPI_REPO_URL`: URL du repository, pointe par défaut sur le pypi de test
- `PYPI_API_TOKEN`: Token API définit (dans l'interface web pypi.org, dans `Paramètres du compte > Jetons d'API`)

Vous pouvez définir à minima la variable `PYPI_API_TOKEN` dans l'interface gitlab de votre repository dans `Settings > CI/CD > variables`

## Commandes

### Mise en place de l'environement de developpement

```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
pre-commit install
```

Le requirements.txt est un raccourci pour `pip install -e .`.
Une fois executé, les scripts définis dans [./pyproject.toml](./pyproject.toml) sont disponibles dans le shell local:

```bash
pip install -e .
python-library-template
```

**Vous pouvez utiliser pipx pour rendre le script disponible de manière globale**

```bash
pipx install .
```

### Construire le package

```bash
python -m build
```

### Tests

```bash
pytest
```

### Déployer manuellement

```bash
rm -rf dist/*
python -m build
# A vous de définir les variables
twine upload --repository-url "$PYPI_REPO" -u __token__ -p "$PYPI_TOKEN" dist/*
```
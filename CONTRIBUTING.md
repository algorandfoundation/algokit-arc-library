# AlgoKit ARC Library

All implementations within the official Algorand Foundation repository (https://github.com/algorandfoundation/algokit-arc-library) need to be audited and implement a finalised ARC standard. Initial contributions will be from Algorand Foundation only, but for any enquiries about contribution please email [arcs@algorand.foundation](mailto:arcs@algorand.foundation).

# Setup (AlgoKit ARC Library development)
The following sections provide details on how the development environment for this library should be setup.

## Initial setup

1. Clone this repository: `git clone https://github.com/algorandfoundation/algokit-arc-library`
2. Install pre-requisites:
    - Install `Python` - [Link](https://www.python.org/downloads/): The minimum required version is `3.10`. It is also recommended to use `3.10` for development so dependencies on higher versions are not introduced, and to avoid debugging issues with `3.11`(see https://github.com/fabioz/PyDev.Debugger/issues/234 and https://github.com/microsoft/debugpy/issues/939)
     - Install `Poetry` - [Link](https://python-poetry.org/docs/#installation): The minimum required version is `1.2`.
     - If you're not using PyCharm, then run `poetry install` in the root directory (this should set up `.venv` and install all Python dependencies - PyCharm will do this for you on startup)
3. Install pre-commit hooks (optional but recommended):

   [pre-commit](https://pre-commit.com/) is configured in this repository, so once `poetry install` has been run,
   execute `pre-commit install` inside the virtual-env, and git will ensure formatting, linting, and static typing (via `mypy`)
   is correct when you perform a commit.
4. If you update to the latest source code and there are new dependencies you will need to run `poetry install` again

## Libraries and Tools

AlgoKit uses Python as a main language and many Python libraries and tools. This section lists all of them with a tiny brief.

### Runtime dependencies
- [Beaker](https://algorand-devrel.github.io/beaker/html/index.html): Python framework for building Smart Contracts on Algorand using PyTeal.

### Development dependencies
- [Poetry](https://python-poetry.org/): Python packaging and dependency management.
- [Python Semantic Release](https://python-semantic-release.readthedocs.io/en/latest/): Automatic release versioning based on commits
- [Black](https://github.com/psf/black): A Python code formatter.
- [Ruff](https://github.com/charliermarsh/ruff): A python linter
- [pip-audit](https://pypi.org/project/pip-audit/): A tool for scanning dependencies for known vulnerabilities

## Project Structure
Each ARC implementation in `src` should have a corresponding document in `docs/arcs/[name].md` where name is the name of the class in lowercase.

The documentation should contain the following links:
* The ARC specification implemented e.g. `[ARC-9999](https://arc.algorand.foundation/ARCs/arc-9999)`
* An Audit report for the implementation e.g. `[Audit](https://link/to/audit.pdf)`

There is a simple [test](tests/test_repo_conventions.py) that is used to quickly check that contributions meet these requirements.

## Commits

We are using the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/#summary) standard for commit messages. This allows us to automatically generate release notes and version numbers. We do this via [Python Semantic Release](https://python-semantic-release.readthedocs.io/en/latest/) and [GitHub actions](.github/workflows/cd.yaml).

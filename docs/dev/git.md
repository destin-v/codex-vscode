---
icon: octicons/git-branch-16
---

# :octicons-git-branch-16: Git

## 🎯 Git

```bash
git config --global user.name "Your Name"
```

```bash
git config --global user.email "youremail@yourdomain.com"
```

```bash
git config --global core.editor "nvim"
```

## 📦 uv
Install uv:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Create a new project:
```bash
uv init
```

Edit `pyproject.toml`.

```toml
[project]
name = "myproject"
version = "0.1.0"
description = ""
requires-python = ">=3.12"
authors = ["John Doe"]
license = "MIT"
readme = "README.md"
dependencies = [
    "loguru", 
    "rich",
    "typer",
]
```

Create a new environment:
```bash
uv venv --python 3.12
```

Add dependencies:
```bash
uv add foo
```

To create a lock file:
```bash
uv lock
```

To install the lock file:
```bash
uv sync
```

To install optional dependencies:
```bash
uv sync --extra foo
```

To install with all optional dependencies:
```bash
uv sync --all-extras
```

## 🅿 Pre-commit
Always install/update your pre-commit to use the latest versions prior to starting a project.

```bash
uv run pre-commit install
```

```bash
uv run pre-commit autoupdate
```
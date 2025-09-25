---
icon: fontawesome/solid/wine-bottle
---

# :fontawesome-solid-wine-bottle: Nox

Nox is the spiritual successor to Tox for running scripts in controlled environments.

The `noxfile.py` provides an example of how to run each of these:

```bash
nox --list             # lists out all the available sessions
```

```bash
nox                    # run all tests
```

```bash
nox -s pytest          # run pytest
```

Special sessions are needed for [`lock files`](https://nox.thea.codes/en/stable/cookbook.html#using-a-lockfile):


```python
@nox.session(venv_backend="uv")
def pytest(session: nox.Session) -> None:

    python_path: str = session.virtualenv.location

    session.run_install(
        "uv",
        "sync",
        "--all-extras",
        f"--python={python_path}",
        env={"UV_PROJECT_ENVIRONMENT": python_path},
    )

    session.run("pytest")

```

!!! tip
    For an explanation on how to properly setup multiple versions of Python to run with Nox see [**here**](https://sethmlarson.dev/nox-pyenv-all-python-versions).

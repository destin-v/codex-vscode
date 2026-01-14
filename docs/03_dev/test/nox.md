---
icon: fontawesome/solid/wine-bottle
---

# :fontawesome-solid-wine-bottle: Nox

Nox is the spiritual successor to Tox for running scripts in controlled environments.

The `noxfile.py` provides an example of how to run each of these:

```bash
nox --list  # lists out all the available sessions
```
```console
Sessions defined in noxfile.py:

* pytest-3.12 -> Run PyTest coverage.
* pytest-3.13 -> Run PyTest coverage.
* pytest-3.14 -> Run PyTest coverage.

sessions marked with * are selected, sessions marked with - are skipped.
```

```bash
nox
```
```console
nox > Ran multiple sessions:
nox > * pytest-3.12: success
nox > * pytest-3.13: success
nox > * pytest-3.14: success
```

!!! note

    To run a specific test try `nox -s <TEST>` (i.e. `nox -s pytest`).


## Lock Files
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

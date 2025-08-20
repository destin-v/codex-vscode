# Nox

Nox is the spiritual successor to Tox for running scripts in controlled environments.

* **pytest**: tests the code
* **sphinx**: documentation software

The `noxfile.py` provides an example of how to run each of these:

```bash
nox --list             # lists out all the available sessions
nox -s pytest          # run pytests
nox -s show_sphinx     # view HTML of sphinx
nox -s build           # build pytest & documentation
```

Special sessions are needed for [lock files](https://nox.thea.codes/en/stable/cookbook.html#using-a-lockfile):


```python
@nox.session(venv_backend="uv")
def pytest(session: nox.Session) -> None:
    ...
```

For an explanation on how to properly setup multiple versions of Python to run with Nox see [**here**](https://sethmlarson.dev/nox-pyenv-all-python-versions).

---
icon: material/test-tube
---

# :material-test-tube: Test

## Reports
### [:simple-pytest:            Nox - PyTest - Summary  ](../assets/tests/pytest-summary/index.html)
### [:octicons-checklist-16:    Nox - PyTest - Coverage ](../assets/tests/pytest-coverage/index.html)
### [:material-view-dashboard:  Nox - PyTest - Allure   ](../assets/tests/pytest-allure/index.html)

## 🧪 PyTests

The `tests` folder should mirror `src` to ensure that each submodule is properly tested.  Include an `integration` folder under `tests` to evaluate larger tests.

```
project
└───src
|   └─── __init__.py
│   └───packageA
│       └─── __init__.py
│       └─── A.py
└───tests
    └─── __init__.py
    └─── packageA
         └─── __init__.py
         └─── A_test.py
```

!!! warning
    It is generally recommended that you do not have `tests` in your `src` folder since they would become importable as part of your distribution.

!!! tip
    Tests should include both `unit` and `integration` testing.

```bash
pytest # run all tests
```

```bash
pytest pytest tests/basic_test.py # run tests in module
```

```bash
pytest tests/basic_test.py::test_hello_world # run a specific test
```

!!! info
    PyTest provides additional features such as [parameter sweeping](https://docs.pytest.org/en/7.1.x/example/parametrize.html), [fixtures](https://docs.pytest.org/en/7.1.x/explanation/fixtures.html?highlight=fixtures), and [logging](https://docs.pytest.org/en/7.1.x/how-to/logging.html?highlight=fixtures).  These should be applied depending on the test requirements.

### :octicons-checklist-16: Coverage
PyTests offers `coverage` support.  When running PyTests with Coverage, it will generate a HTML that show which parts of your repo have not been traced using PyTests.  This lets you know which areas of your code still need to be tested.

```bash
pytest --cov=<repo_path> --cov-report=html:<target_output>
```

### :material-view-dashboard: Allure
[Allure](https://allurereport.org/) provides a dashboard that aggregates your pytest results.  Allure provides additional functionality like tagging for your tests to organize them into a tree structure.  In order to use allure, you must install it via Homebrew:

```bash
brew install allure
```

To create and view an Allure report:

```bash
pytest --alluredir <user_directory>  # run pytests
```

```bash
allure generate --single-file --output <output_dir> # generate a report (HTML)
```

## 🧪 Nox

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



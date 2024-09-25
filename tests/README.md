# PyTests
Tests should include both `unit testing` and `integration testing`.  Prior to developing a feature, the tests should be written to verify that the function behaves as expected.  Once the verification function has been written, the function to perform the task should be written.

```bash
pytest # run all tests
pytest pytest tests/basic_test.py # run tests in module
pytest tests/basic_test.py::test_hello_world # run a specific test
```

PyTest provides additional features such as [parameter sweeping](https://docs.pytest.org/en/7.1.x/example/parametrize.html), [fixtures](https://docs.pytest.org/en/7.1.x/explanation/fixtures.html?highlight=fixtures), and [logging](https://docs.pytest.org/en/7.1.x/how-to/logging.html?highlight=fixtures).  These should be applied depending on the test requirements.

## Coverage
PyTests offers `coverage` support.  When running PyTests with Coverage, it will generate a HTML that show which parts of your repo have not been traced using PyTests.  This lets you know which areas of your code still need to be tested.

```console
pytest --cov=<repo_path> --cov-report=html:<target_output>
```

## Allure
[Allure](https://allurereport.org/) provides a dashboard that aggregates your pytest results.  Allure provides additional functionality like tagging for your tests to organize them into a tree structure.  In order to use allure, you must install it via Homebrew:

```console
brew install allure
```

To create and view an Allure report:

```console
pytest --alluredir <user_directory>  # run pytests
allure generate --single-file --output <output_dir> # generate a report (HTML)
```

## Design Pattern
The `tests` folder should mirror what you have in `src` to ensure that each submodule is properly tested.  You can include a `integration` folder under `tests` to evaluate larger tests.

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

It is generally recommended that you do not have `tests` in your `src` folder since they would become importable as part of your distribution.

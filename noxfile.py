import os
from dataclasses import dataclass

import nox

from src.ci.browser import view_html


@dataclass
class config:
    """Configurations."""

    # Pytest
    pytest_path_allure_html: str = "docs/source/_static/pytest-allure-html"
    pytest_path_allure_build: str = "docs/source/_static/pytest-allure-build"
    pytest_path_coverage: str = "docs/source/_static/pytest-coverage"
    pytest_path_summary: str = "docs/source/_static/pytest-summary"

    # Documentation
    sphinx_path: str = "docs/build/html"


def install_uv_env(session: nox.Session) -> None:
    """Install a uv environment for a Nox session.

    Args:
        session (nox.Session): _description_
    """
    python_path: str = session.virtualenv.location
    session.run_install(
        "uv",
        "sync",
        "--all-extras",
        f"--python={python_path}",
        env={"UV_PROJECT_ENVIRONMENT": python_path},
    )


@nox.session(venv_backend="uv")
def pytest(session: nox.Session) -> None:
    """Run PyTest coverage.

    Args:
        session (nox.Session): The current Nox session.
    """

    install_uv_env(session)

    session.run(
        "pytest",
        "--verbosity=3",
        # -------------- Coverage --------------
        "--cov=./",
        f"--cov-report=html:{config.pytest_path_coverage}",
        # -------------- Summary --------------
        f"--html={config.pytest_path_summary}/index.html",
        "--self-contained-html",
        # -------------- Allure --------------
        f"--alluredir={config.pytest_path_allure_build}",
        # -------------- Mem Ray --------------
        "--memray",
    )

    # Cleanup
    session.run("mv", ".coverage", config.pytest_path_coverage, external=True)


@nox.session
def allure(session: nox.Session) -> None:
    """Create an Allure report.

    Args:
        session (nox.Session): The current Nox session.
    """

    if os.path.exists(config.pytest_path_allure_build) is False:
        print("Allure build not found, exiting...")
        return

    # Allure report generation
    try:
        session.run(
            "allure",
            "generate",
            "--single-file",
            "--clean",
            "--output",
            config.pytest_path_allure_html,
            config.pytest_path_allure_build,
            external=True,
        )
    except Exception:
        print("Allure report failed to generate, have you installed Allure via homebrew?")


@nox.session(venv_backend="uv")
def sphinx(session: nox.Session) -> None:
    """Generate Sphinx documentation.

    Args:
        session (nox.Session): The current Nox session.
    """
    install_uv_env(session)

    # Build Sphinx
    session.run("sphinx-apidoc", "-o", "docs/source/pages/api/src", "src")
    session.run("sphinx-apidoc", "-o", "docs/source/pages/api/tests", "tests")
    session.chdir("docs")
    session.run("make", "clean", external=True)
    session.run("make", "html", external=True)
    session.chdir("../")


@nox.session
def show_pytest(session: nox.Session) -> None:
    """Show pytest coverage in HTML.

    Args:
        session (nox.Session): The current Nox session.
    """

    pytest(session)
    allure(session)

    view_html(config.pytest_path_summary)
    view_html(config.pytest_path_coverage)
    view_html(config.pytest_path_allure_html)


@nox.session
def show_sphinx(session: nox.Session) -> None:
    """Show Sphinx in HTML.

    Args:
        session (nox.Session): The current Nox session.
    """

    sphinx(session)

    view_html(config.sphinx_path)

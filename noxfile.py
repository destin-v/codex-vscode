import nox
from rich import print
from rich.panel import Panel


def install_uv_env(session: nox.Session) -> None:
    """Install a uv environment for a Nox session.

    Args:
        session (nox.Session): _description_
    """

    print(Panel("🧰 Constructing Virtual Environment"))

    python_path: str = session.virtualenv.location
    session.run_install(
        "uv",
        "sync",
        "--all-extras",
        f"--python={python_path}",
        env={"UV_PROJECT_ENVIRONMENT": python_path},
    )


@nox.session(venv_backend="uv", python=["3.12", "3.13", "3.14"])
def pytest(session: nox.Session) -> None:
    """Run PyTest coverage.

    Args:
        session (nox.Session): The current Nox session.
    """

    install_uv_env(session)
    session.run( "pytest",  "--rich")
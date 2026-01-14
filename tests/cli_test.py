from typer.testing import CliRunner

from src.main import app

runner = CliRunner()


def test_app_hello_world():
    result = runner.invoke(app, ["hello-world", "--name", "Bob"])
    assert result.exit_code == 0
    assert "Hello Bob!" in result.output


def test_app_progress_bar():
    result = runner.invoke(app, ["progress-bar"])
    assert result.exit_code == 0


def test_app_table():
    result = runner.invoke(app, ["table"])
    print(result.output)
    assert result.exit_code == 0

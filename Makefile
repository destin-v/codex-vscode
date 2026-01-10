help:
	@echo "make [command]:"
	@echo "---------------"
	@echo "setup:       Installs the repository."
	@echo "test:        Run tests."
	@echo "run:         Run application."
	@echo "cleanup:     Cleanup generated files."

setup:
	uv venv --python 3.14
	source .venv/bin/activate
	uv sync --all-extras

test:
	pytest

run: 
	@echo "Run"

clean:
	rm -rf .cache
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf site

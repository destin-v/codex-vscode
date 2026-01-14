# Variables
PATH_ALLURE_REPORT=test-reports/pytest-allure-html
PATH_ALLURE_BUILD=test-reports/pytest-allure-build
PATH_PYTEST_COVERAGE=test-reports/pytest-coverage
PATH_PYTEST_SUMMARY=test-reports/pytest-summary
PATH_PYPROJECT=pyproject.toml

help:
	@echo "make [command]:"
	@echo "---------------"
	@echo "setup:       Installs the repository."
	@echo "test:        Run tests."
	@echo "reports:   	Generate test reports with Coverage and Allure."
	@echo "run:         Run application."
	@echo "cleanup:     Cleanup generated files."

setup:
	uv venv --python 3.14
	source .venv/bin/activate
	uv sync --all-extras

test:
	pytest --rich

reports:
	# Pytest, Coverage, Allure reports.
	# Note
	# 	* Requires `pytest`, `coverage`, `allure` to be installed via Homebrew or apt-get.

	pytest \
		--rich \
		--cov=./ \
		--cov-config=${PATH_PYPROJECT} \
		--cov-report=html:${PATH_PYTEST_COVERAGE} \
		--html=${PATH_PYTEST_SUMMARY}/index.html \
		--self-contained-html \
		--alluredir=${PATH_ALLURE_BUILD}

	mv .coverage ${PATH_PYTEST_COVERAGE}/

	allure \
        generate \
        --single-file \
        --clean \
        --output \
        ${PATH_ALLURE_REPORT} \
        ${PATH_ALLURE_BUILD}

	@echo "------------------- Test Reports -------------------"
	@echo "Pytest Report   @ ./${PATH_PYTEST_SUMMARY}/index.html"
	@echo "Coverage Report @ ./${PATH_PYTEST_COVERAGE}/index.html"
	@echo "Allure Report   @ ./${PATH_ALLURE_REPORT}/index.html"

run:
	python src/main.py -h

clean:
	# https://www.techgrind.io/explain/what-is-the-best-way-to-clear-out-all-the-__pycache__-folders-and-pycpyo-files-from-a-python3-project

	# Remove top level directories.
	rm -rf .cache
	rm -rf .nox
	rm -rf logs
	rm -rf site

	# Remove generated folders in sub-directories.
	find . -type d -name "__pycache__" 		-exec rm -r {} +
	find . -type d -name ".mypy_cache"		-exec rm -r {} +
	find . -type d -name ".pytest_cache"	-exec rm -r {} +

	# Remove all .pyc and .pyo files.
	find . -type f -name "*.pyc" 			-exec rm -f {} +
	find . -type f -name "*.pyo" 			-exec rm -f {} +

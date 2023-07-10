VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

virtual_env:
	python3 -m venv $(VENV)

install: virtual_env
	 $(PIP) install -r requirements-dev.txt

run_test:
	${PYTHON} -m pytest --cov-fail-under=90 --cov=hooks test/

lint:
	${PYTHON} -m flake8 hooks
	${PYTHON} -m pylint hooks

build: clean install pre-commit
	make lint
	make run_test

clean:
	rm -rf .coverage
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf __pycache__
	rm -rf $(VENV)

pre-commit:
	pre-commit clean
	pre-commit install -t prepare-commit-msg -t pre-push
	pre-commit autoupdate

.PHONY: virtual_env install run_test lint prepre clean pre-commit

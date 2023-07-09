VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

virtual_env:
	python3 -m venv $(VENV)

install: virtual_env
	 $(PIP) install -r requirements.txt

run_test:
	${PYTHON} -m pytest --cov=hooks test/

lint:
	${PYTHON} -m flake8 hooks
	${PYTHON} -m pylint hooks

build: clean install
	make lint
	make run_test

clean:
	rm -rf .coverage
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf __pycache__
	rm -rf $(VENV)

.PHONY: virtual_env install run_test lint prepre clean

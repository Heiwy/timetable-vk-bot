# Python3 executable
PYTHON = .venv/bin/python3

# Code sources directory
SOURCES = sources

.PHONY: run lint

run: lint
	${PYTHON} ${SOURCES}/wsgi.py

lint:
	flake8 --ignore F401 ${SOURCES}

venv:
	python3 -m venv .venv
	${PYTHON} -m pip install -r requirements.txt

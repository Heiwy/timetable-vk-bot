# Python3 executable
PYTHON = .venv/bin/python3

# Code sources directory
SOURCES = sources

.PHONY: run lint

run: lint
	${PYTHON} ${SOURCES}/wsgi.py

lint:
	flake8 ${SOURCES}

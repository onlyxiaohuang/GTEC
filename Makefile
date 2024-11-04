#for ubuntu version
PYTHON = /bin/python3

makedir := $(shell pwd)
testdir := $(makedir)/src/test.py


requirements:
	$(PYTHON) -m pip install requests

test_variable:
	@echo makedir = $(makedir)
	@echo testdir = $(testdir)

test: requirements
	@echo "Running tests in native mode."
	$(PYTHON) -O $(testdir)


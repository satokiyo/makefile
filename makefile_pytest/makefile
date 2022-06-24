PYTHON?=python3.10
WORKDIR?=$(shell pwd)
REQUIREMENTS_TXT?=$(wildcard requirements.txt)
REQUIREMENTS_TEST_TXT?=$(wildcard requirements_test.txt)
VENVDIR?=$(WORKDIR)/venv
VENV?=$(VENVDIR)/bin
VENVDIR_TEST?=$(WORKDIR)/venv_test
VENV_TEST?=$(VENVDIR_TEST)/bin
TEST_TARGETS?=$(wildcard test_*.py) $(wildcard $(WORKDIR)/tests/test_*.py) $(wildcard $(WORKDIR)/mypackage/tests/test_*.py)
SRC_SCRIPTS?=$(wildcard $(WORKDIR)/mypackage/src/mypackage/*.py)
EXE=

# windows?
ifeq (win32,$(shell $(PYTHON) -c "import __future__, sys; print(sys.platform)"))
EXE=.exe
endif

.PHONY: venv
venv:
	[ -d $(VENVDIR) ] || ($(PYTHON) -m venv $(VENVDIR) && $(VENV)/python -m pip install --upgrade pip setuptools wheel && $(VENV)/python -m pip install -r $(REQUIREMENTS_TXT))
	. $(VENV)/activate

.PHONY: venv_test
venv_test:
	[ -d $(VENVDIR_TEST) ] || ($(PYTHON) -m venv $(VENVDIR_TEST) && $(VENV_TEST)/python -m pip install --upgrade pip setuptools wheel && $(VENV_TEST)/python -m pip install -r $(REQUIREMENTS_TEST_TXT))
	. $(VENV_TEST)/activate

.PHONY: clear-venv
clear-venv:
	rm -r "$(VENVDIR)"

.PHONY: show-venv
show-venv: venv
	@$(VENV)/python -c "import sys; print('Python ' + sys.version.replace('\n', ''))"
	@$(VENV)/pip --version
	@echo venv: $(VENVDIR)

.PHONY: debug-venv
debug-venv: venv
	@echo "PATH (Shell)=$$PATH"
	@$(MAKE) --version
	$(info PATH (GNU Make)="$(PATH)")
	$(info SHELL="$(SHELL)")
	$(info PY="$(PY)")
	$(info REQUIREMENTS_TXT="$(REQUIREMENTS_TXT)")
	$(info SETUP_PY="$(SETUP_PY)")
	$(info SETUP_CFG="$(SETUP_CFG)")
	$(info VENVDIR="$(VENVDIR)")
	$(info VENVDEPENDS="$(VENVDEPENDS)")
	$(info WORKDIR="$(WORKDIR)")


.PHONY: python
python: venv
	exec $(VENV)/python

.PHONY: run
run: venv
	exec $(VENV)/python $(WORKDIR)/mypackage/src/mypackage/mypackage.py

.PHONY: test
test: venv_test
	exec $(VENV_TEST)/python -m pytest -v -s --cov=mypackage -W ignore::DeprecationWarning

.PHONY: doc
doc:
	exec $(VENV_TEST)/python -m pydoc -w document $(SRC_SCRIPTS)
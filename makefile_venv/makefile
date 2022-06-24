PYTHON?=python3.10
WORKDIR?=$(shell pwd)
REQUIREMENTS_TXT?=$(wildcard requirements.txt)
VENVDIR?=$(WORKDIR)/venv
VENV?=$(VENVDIR)/bin
EXE=

# windows?
ifeq (win32,$(shell $(PYTHON) -c "import __future__, sys; print(sys.platform)"))
EXE=.exe
endif

.PHONY: venv
venv:
	[ -d $(VENVDIR) ] || ($(PYTHON) -m venv $(VENVDIR) && $(VENV)/python -m pip install --upgrade pip setuptools wheel && $(VENV)/python -m pip install -r $(REQUIREMENTS_TXT))
	. $(VENV)/activate

.PHONY: clean-venv
clean-venv:
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
	exec $(VENV)/python $(WORKDIR)/python/main.py

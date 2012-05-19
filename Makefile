
##########
# defaults

SRC=src
BIN=bin

# Python virtualenv location
PYENV=.pyenv

# custom pip script ignores/filters "already installed, use --upgrade" and "cleaning up" msgs
PIP=$(BIN)/pip_

PROJECT_NAME=ppk

# project abbreviated name
PROJECT_ABBREV=$(PROJECT_NAME)

# - initial "default" rule
# will be used it you just type "make" on the cmdline


##########
# keep VAR assignments above so can be overridden by users

-include inc/*.mk

##########

.PHONY: all
all: install clean
# I like to cleanup Python projects after every run

# I like to cleanup Python projects after every run
.PHONY: install
install: deploy clean

.PHONY: depends
depends:
	@$(PIP) install nose

.PHONY: compile
compile: depends

# automatically run tests every time a file changes
.PHONY: autotest
autotest:
	@$(BIN)/autotest

.PHONY: test
test: compile
	@nosetests $(SRC)/test

.PHONY: deploy
# TBD put code up somewhere, etc
deploy: test

.PHONY: clean
clean:
	@find $(SRC) -type f -name \*.pyc -print0 | xargs -0 rm -rf

# purposely don't "rm -rf" the $(PYENV) b/c of risk of bad values wiping a homedir, etc
.PHONY: realclean distclean
realclean: distclean
distclean: clean
	@-rm -f $(BIN)/virtualenv.py
	@-rm -f .ci_*


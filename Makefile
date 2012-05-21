
##########
# defaults

SRC=src
BIN=bin

# custom pip script ignores/filters "already installed, use --upgrade" and "cleaning up" msgs
PIP=$(BIN)/pip_

PROJECT_NAME=pytimecop

# project abbreviated name
PROJECT_ABBREV="ptc"

NOSE_FLAGS="--nocapture"


##########
# - initial "default" rule
# will be used it you just type "make" on the cmdline
.PHONY: all
all: install clean
# I like to cleanup Python projects after every run

# Includes need to be below the default "all" command or rules defined
# in them will be interpreted as the default/first rule

##########
# keep VAR assignments above so can be overridden by users

-include inc/*.mk

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
	@nosetests $(SRC)/test $(NOSE_FLAGS)

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


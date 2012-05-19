
# rules for bootstrapping a virtualenv to work in
# useful if you get errors about not having pip, etc. :)

.PHONY: bootstrap
# use system python to setup a local virtualenv
bootstrap: $(PYENV)

$(PYENV): $(BIN)/virtualenv.py 
	@python $(BIN)/virtualenv.py --distribute --prompt='($(PROJECT_ABBREV)) ' $(PYENV)
	@-rm distribute-*.tar.gz

# you can always put your own version there and we'll leave it alone
$(BIN)/virtualenv.py:
	@echo "Downloading virtualenv from GitHub"
	@curl https://raw.github.com/pypa/virtualenv/master/virtualenv.py > $(BIN)/virtualenv.py


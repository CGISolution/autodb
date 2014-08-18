
VERSION = 1.2

PYTHON = $(shell test -x bin/python && echo bin/python || echo `which python`)
#PYVERS = $(shell $(PYTHON) -c 'import sys; print "%s.%s" % sys.version_info[0:2]')
BUILD_NUMBER ?= 1

all:
	$(PYTHON) autodb.py autodb

clean:
	@echo "Removing .pyc"

debian/changelog:
	git branch -D changelog
	git checkout -b changelog
	git-dch -a -N $(shell $(SETUP) --version) --debian-branch changelog --snapshot --snapshot-number=$(BUILD_NUMBER)

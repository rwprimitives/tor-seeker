PACKAGE := $(shell cat setup.cfg | grep -E "^name\s*=\s*([^']*)" | cut -d "=" -f2 | xargs)


.PHONY: all
.PHONY: clean

all: build-pip

build-pip:
	python3 -m build .

install: build-pip
	python3 -m pip install .

uninstall:
	python3 -m pip uninstall ${PACKAGE} -y

clean:
	rm -rf src/*.egg-info
	rm -rf dist
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

help:
	@echo "The following targets are available:"
	@echo ""
	@echo "build-pip: Generates distributions packages (ie: *.whl and *.tar.gz)"
	@echo "install:   Installs distribution package"
	@echo "uninstall: Uninstalls distribution package"
	@echo "clean:     Removes any automatically generated files"
	@echo  ""

# Get the name of the package from the setup.cfg file
PACKAGE := $(shell cat setup.cfg | grep -E "^name\s*=\s*([^']*)" | cut -d "=" -f2 | xargs)


.PHONY: all

all: build-pip

build-pip:
	python3 -m build .

build-deb:
	python3 setup.py --command-packages=stdeb.command bdist_deb

install-pip: build-pip
	python3 -m pip install .

install-deb: build-deb
	sudo dpkg -i deb_dist/python3-torseeker*.deb

uninstall-pip:
	python3 -m pip uninstall ${PACKAGE} -y

uninstall-deb:
	sudo dpkg -r python3-torseeker

clean:
	rm -rf src/*.egg-info
	rm -rf deb_dist
	rm -rf dist
	rm -rf *.gz
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

help:
	@echo "The following build targets are available:"
	@echo ""
	@echo "build-pip:     Generates distributions packages (ie: *.whl and *.tar.gz)"
	@echo "build-deb:     Generates Debian Linux distribution package (ie: *.deb)"
	@echo "install-pip:   Builds and installs distribution package"
	@echo "uninstall-pip: Uninstalls distribution package"
	@echo "clean:         Removes any automatically generated files"
	@echo  ""

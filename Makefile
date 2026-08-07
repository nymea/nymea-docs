BRANCH ?= master
SPHINXBUILD ?= sphinx-build
SOURCEDIR = docs
BUILDDIR = public

.PHONY: generate html clean serve

generate:
	python3 tools/generate-sphinx-docs.py --branch $(BRANCH)

html:
	$(SPHINXBUILD) -b html $(SOURCEDIR) $(BUILDDIR) -W --keep-going

clean:
	rm -rf $(BUILDDIR)
	rm -rf docs/documentation/resources/integrations
	rm -rf docs/documentation/resources/api
	rm -rf docs/documentation/resources/changelog
	rm -f docs/documentation/resources/interfaces.rst
	rm -f docs/documentation/developers/clients/raw-api.rst
	rm -f docs/documentation/developers/integrations/plugin-json.rst

serve:
	python3 -m http.server 8000 --directory $(BUILDDIR)

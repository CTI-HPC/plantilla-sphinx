SPHINXBUILD   = sphinx-build
SPHINXOPTS    = -q -D latex_paper_size=letter
BUILDDIR      = build
ALLSPHINXOPTS = -d $(BUILDDIR)/doctrees $(SPHINXOPTS) source

OPEN = xdg-open
DEPLOYDIR = rbonvall@hpc.cl:public_html/plantilla

.PHONY: all open help clean html epub latex latexpdf linkcheck

all: html

open:
	@$(OPEN) $(BUILDDIR)/html/index.html

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files"
	@echo "  latex      to make LaTeX files"
	@echo "  epub       to make an epub"
	@echo "  linkcheck  to check all external links for integrity"
	@echo "  open"
	@echo "  clean"
	@echo "  deploy"

clean:
	-rm -rf $(BUILDDIR)/*

html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

epub:
	$(SPHINXBUILD) -b epub $(ALLSPHINXOPTS) $(BUILDDIR)/epub
	@echo
	@echo "Build finished. The epub file is in $(BUILDDIR)/epub."

latex:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo
	@echo "Build finished; the LaTeX files are in $(BUILDDIR)/latex."
	@echo "Run \`make' in that directory to run these through (pdf)latex" \
	      "(use \`make latexpdf' here to do that automatically)."

linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."

deploy: html
	@echo "Deploying..."
	rsync -a $(BUILDDIR)/html/ $(DEPLOYDIR)


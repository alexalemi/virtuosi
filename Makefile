PELICAN=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)/site
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

WGET:=$(shell which wget)
PYTHON:=$(shell which python)
MATHJAXURL=https://raw.github.com/mayoff/python-markdown-mathjax/master/mdx_mathjax.py
MATHJAXFILE=$(shell find .env -iname site-packages)/markdown/extensions/mathjax.py

.PHONY: html help clean regenerate serve devserver publish ssh_upload rsync_upload dropbox_upload ftp_upload github

help:
	@echo 'Makefile for a pelican Web site                                        '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make create_env                  create the virtual env             '
	@echo '   make mathjax                     Install the mathjax plugin         '
	@echo '   make html                        (re)generate the web site          '
	@echo '   make clean                       remove the generated files         '
	@echo '   make regenerate                  regenerate files upon modification '
	@echo '   make publish                     generate using production settings '
	@echo '   make serve                       serve site at http://localhost:8000'
	@echo '   make devserver                   start/restart develop_server.sh    '
	@echo '   make github                      upload the web site via gh-pages   '
	@echo '                                                                       '

create_env: 
	virtualenv -p ${PYTHON} --no-site-packages --distribute .env && . .env/bin/activate && pip install -r requirements.txt
	make mathjax

mathjax: 
ifdef WGET
	wget ${MATHJAXURL} -O ${MATHJAXFILE}
else
	curl ${MATHJAXURL} > ${MATHJAXFILE}
endif

html: clean $(OUTPUTDIR)/index.html
	@echo 'Done'

$(OUTPUTDIR)/%.html:
	cd $(BASEDIR); $(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	find $(OUTPUTDIR) -mindepth 1 -delete

regenerate: clean
	cd $(BASEDIR); $(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
	cd $(OUTPUTDIR) && python -m SimpleHTTPServer

devserver:
	cd $(BASEDIR); ./develop_server.sh restart

publish:
	cd $(BASEDIR); $(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

github: publish
	ghp-import $(OUTPUTDIR)
	git push origin gh-pages

A New Virtuosi
==============

[http://thephysicsvirtuosi.com](http://thephysicsvirtuosi.com)

An attempt at making a new virtuosi site, using [Pelican](http://getpelican.com)

This is meant to be a collaborative site for interesting physics posts, geared towards
a general audience.

Contributing
------------

Feel free to contribute your post ideas.

Before you begin, make sure you have virtualenv and Python installed.  Due
to updates in `pelican`, it is recommended to have Python 2.7.x or later.  

To create the virtual environment, use the script `make create_env`, which will
create a folder `./.env` which contains pelican and its dependencies which we
will use to develop.  If you have side by side installations of Python, you can
specify which to use in this environment by making sure `which python` returns
the one you expect by modifying the PATH environment variable, e.g.
`PATH=/your/path/to/python/bin:${PATH} make create_env`.

Every time you come back to modify the site, you should switch your Python
environment back to the one we just created.  To do so, run `source source_env`
or `source .env/bin/activate` in the root directory or the project.  When you
do this, you should see your command line change so that it starts with a
`(.env)` at the start of the prompt, this shows that you are in the virtual
environment.  To exit the virtual environment, use `deactivate`.

From here:

 * Write a markdown or restructed text file somewhere in `site/content/`
 * In the root directory, run `make html` to build the pages
 * Test your build with `make serve` or `make devserver` in the /site/ directory
 * This will serve the site at `http://localhost:8000/`
 * Make sure you haven't broken anything.
 * If you like what you see, commit the change and submit a pull request at github.
 * Your post will be reviewed and possibly accepted.

Note if you are using the devserver, you might want to change the SITEURL in
pelicanconf.py to be `http://localhost:8000` while you are editing, so that
your links all work.

Checkout `post_template.md` for an example post in markdown format, 
fill out as many tags as you can to make the post behave well.

Code Outline
------------
 * `Makefile` - some useful make utilities, try running `make`
 * `create_env` - create the virtual environment defined in `requirements.txt` in the `.env` directory
 * `post_template.md` - an example post in markdown format with metadata defined at the top
 * `requirements.txt` - the packages used in the virtual environment
 * `source_env` - sources the virtual environment, same as `source .env/bin/activate`
 * `/tools` - miscellaneous scripts used during the migration from blogspot.
 * `/site` - the site itself
   * `/content` - the posts in markdown, restructured text or html format.
   * `/themes` - the themes for the site itself.
   * `Makefile` - convience makefile for building / testing / viewing the site (try typing `make` while in the `site` directory to see the options )
   * `pelicanconf.py` - the site settings.

Guidelines
----------

Posts on the virtuosi are meant to be fun and interesting first and foremost.  They ought to be tangentially related to physics,
or science in general.  They should be digestable by a more-or-less general audience.  They should be well thought out.


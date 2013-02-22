A new virtuosi
==============

[http://thephysicsvirtuosi.com](http://thephysicsvirtuosi.com)

An attempt at making a new virtuosi site, using [Pelican](http://getpelican.com)

Editing
-------

Before you begin, make sure you have virtualenv and python installed.

To create the virtualenvironment we'll use, use the script `create_env`,
this will create a virtual environment in the directory `.env` that we will 
use to develop.

To source this environment to ensure you have the right versions of the
packages, use the `source_env` script.  Or use `source .env/bin/activate`

From here:

 * write a markdown or restructed text file somewhere in `site/content/`
 * test your build with `make devserver` in the /site/ directory
 * this will serve the site at `http://localhost:8000/`
 * make sure you haven't broken anything.
 * when satisfied, use `update_site` script
 * this will replace the real website

Checkout `post_template.md` for an example post in markdown format, fill out as many tags as you can to make the post behave well.

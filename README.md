A new virtuosi
==============

[http://thephysicsvirtuosi.com](http://thephysicsvirtuosi.com)

An attempt at making a new virtuosi site, using [Pelican](http://getpelican.com)

Editing
-------

Before you begin, make sure you have virtualenv and python installed.

To create the virtualenvironment we'll use, use the script `create_env`, 
but run it with source, i.e. `source create_env`
this will create a virtual environment in the directory `.env` that we will 
use to develop, and source the virtual env for you, you shoulde see your 
command line change so that it starts with a `(.env)` at the start of the prompt, 
this shows that you are in the virtual environment.

To source this environment, if you are coming back later, that is you've already 
created the environment but are starting a new editing session, use `source source_env` 
or `source .env/bin/activate`. 
To exit the virtual environment, use `deactivate`.

From here:

 * write a markdown or restructed text file somewhere in `site/content/`
 * test your build with `make devserver` in the /site/ directory
 * this will serve the site at `http://localhost:8000/`
 * make sure you haven't broken anything.
 * If you like what you see, commit the change and submit a pull request at github.
 * your post will be reviewed and possibly accepted.

Checkout `post_template.md` for an example post in markdown format, 
fill out as many tags as you can to make the post behave well.



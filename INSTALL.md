# INSTALL

To get the virtual environment setup, use virtualenv

    virtualenv -p $(shell which python) .env

Then source the environment

    source .env/bin/activate

Then install the dependencies

    pip install -r requirements.txt

Then make sure mathjax works with

    make mathjax

You should be good to go....  Hopefully.

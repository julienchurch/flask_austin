#Hi, Austin.

I'm slightly drunk and this is a basic Flask app. I'm using a freshly-installed Ubuntu 14.04, so there should be no discrepancies between our systems. 

This assumes you have the following installed before moving forward:

* Python 3.X
* pip
* virtualenv
* PostgreSQL
* libpq-dev

None of this will work without these! If you need any guidance on how to install something or its dependencies, just gimme a shout.

##Step 1

Because of the way `pip` hardcodes paths, **you're going to have to create a virtualenv and install the dependencies on your system** via the following commands:

    cd /path/to/cloned/repo
    virtualenv venv
    . venv/bin/activate
    pip install -r requirements.txt

This will give you access to all your necessary Python packages. If something fails, there's probably a dependency missing somewhere; read through the error message and `apt-get install` whatever it's whining about. Failing that, gimme a call.



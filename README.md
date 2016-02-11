# Project introduction

The purpose of this project is to hold Python programming code related
to TeamDynamix.

# Dependencies

The API portion of this code has now been moved to
[borwick/tdapi](https://github.com/borwick/tdapi).

# Folders within this project

* `app`: Django code (currently empty)
* `requirements`: Helpful starter requirements depending on what
  environment you're in, e.g. development vs. production.
* `td`: Django settings.

# How to start

## Python virtualenv ##

The below will set up a virtual environment for this project called `td`:

    mkvirtualenv td
    pip install -r requirements/dev.txt

You should make sure to use this virtual environment whenever you use
this code.

## Generating a Django secret key ##

    from django.utils.crypto import get_random_string

    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    get_random_string(50, chars)

## Your local settings ##

Create `td/settings/local_settings.py` and put in it...

		SECRET_KEY='put-django-secret-key-here'
        BEID='beid-string-goes-here'
        WebServicesKey='web-services-key-goes-here'

The source for `BEID` and `WebServicesKey` is in TeamDynamix on the
home page of the Admin app.

# How to use

The code in `td/settings/common.py` will create a Django setting
called `TD_CONNECTION`. This is then used by the API to let you do
things like this:

    from tdapi.project import TDProject
    current_projects = TDProject.objects.current()
	for project in current_projects:
	    url = project.td_url
		start_date = project.start_date

# Heads up/issues #

Eventually I will try to remove the Django dependency in `tdapi`, at
which point there may be more things to do in your Django settings
file to create the TeamDynamix connection.

# Project introduction

The purpose of this project is to hold Python programming code related
to TeamDynamix.

# Folders within this project

* `api`: A Python API to TeamDynamix
* `app`: Django code (currently empty)

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

So, the useful stuff is in the `api` subdirectory. When you run any
code within this Django project, a setting `TD_CONNECTION` will be
set. This connection lets you do a bunch of stuff. On one level, you
can call

    resp = settings.TD_CONNECTION.json_request(
	                          method='post',
                              url_stem='projectrequests',
                              data={'Name': name,
                                    'AccountID': ACCOUNT_ID,
                                    'TypeID': PROJECT_TYPE_ID,
                                    'Description': desc,
                                }

referring to the TD REST API for the method, url_stem, and data
parameters. `resp` in the above example will be a Python structure.

There are also a few fancier Python classes for selected elements of
the TD API. These let you interact with TeamDynamix in a more Django-y
way. For example:

    from api.project import TDProject
    current_projects = TDProject.objects.current()
	for project in current_projects:
	    url = project.td_url
		start_date = project.start_date

These aren't really well-documented; the best way to see what exists
is to look in the `api` directory. Generally speaking, there's basic
stuff for Projects, Assets, and CMDB items.

# Writing your own stuff #

You can use `TDAsset` as a model for creating a new Python object.
Basically, you need at least the below code:

    class TDWhateverManager(api.obj.TDObjectManager): pass
	class TDWhatever(api.obj.TDObject): pass
	api.obj.relate_cls_to_manager(TDWhatever, TDWhateverManager)

this `relate_cls_to_manager` function creates `TDWhatever.objects` and
it also tells `TDWhateverManager` about `TDWhatever` so that it can
instantiate objects correctly.

The `api.obj` code is a thin wrapper over the "raw" JSON code.

## Making your stuff somewhat useful ##

If you wanted to then make these classes useful, you would do the following:

### On the manager ###

Create a way to create objects, for example:

    class TDWhateverManager(api.obj.TDObjectManager):
	  def search(self, search_params):
	    return [self.object_class(td_struct)
		        for td_struct
			    in settings.TD_CONNECTION.json_request_roller(
				    method='post',
					url_stem='whatever/search',
					data=search_params)]

(The aforementioned `relate_cls_to_manager` populates `self.object_class`.)

### On the class ###

Create methods as needed, for example:

    class TDWhatever(api.obj.TDObject):
	   def name(self):
	     return self.td_struct['Name']


# Heads up/issues

This code now uses `requests_cache` with a default cache expiration of
1500s. So, if you've been updating TD, the updates may not take effect
for up to 15 minutes.

This code is adapted from some internal code so there may be some
cruft (e.g. weird Python requirements) that are not actually needed
for what you see here.

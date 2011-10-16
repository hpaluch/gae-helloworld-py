GAE Helloworld - experimental python 2.7/concurrent branch
==========================================================

__This is experimental version for new python2.7 environment with concurrent requests (threading support)__ See master branch for traditional python 2.5 version

This is the most simplest application for
Google Application Engine http://code.google.com/appengine/

Additionally to Hello world phrase it also prints current date/time 
to ensure that you are seeing uptodate content.

Setup
-----

* Get GAE SDK for Python from http://code.google.com/appengine/downloads.html#Google_App_Engine_SDK_for_Python. Note - you should use at least version 1.5.5
* install that SDK somewhere, for example:

		su - # go to root, or maybe try 'sudo bash'
		cd /opt
		unzip ~/path_to_my_sdk/google_appengine_1.5.5.zip

Running application localy
--------------------------

__This it not yet supported for GAE version 1.5.5 - only live deployment work for now.__

* change your working directory to this git project, i.e.:

		cd gae-helloworld-py

* run development server

		/opt/google_appengine/dev_appserver.py helloworld

* point you browser to http://localhost:8080

Deploying application to remote GAE
-----------------------------------

* you need to have valid GAE Account - sign on http://code.google.com/appengine/

* you should create new Python application on your GAE Account (this is done via Web inteface). The instance is required to use __HR DataStore__ (requirement of GAE Python 2.7 environment)

* once application is created on GAE you may deploy it:

		/opt/google_appengine/appcfg.py update -A your_app_id helloworld

* the application should be ready on your GAE site (usually something like `http://your_app_id.appspot.com'


Live demo
---------
Is available on http://hp-hello27.appspot.com/

Credits
-------

This (trivial) application is based on http://code.google.com/appengine/docs/python/gettingstartedpython27/helloworld.html

This project is licensed as Public Domain.



GAE Helloworld - Python version
===============================

This is the most simplest application for
Google Application Engine http://code.google.com/intl/cs/appengine/

Additionally to Hello world phrase it also prints current date/time 
to ensure that you are seeing uptodate content.

Setup
-----

* Get GAE SDK for Python from http://code.google.com/intl/cs/appengine/downloads.html#Google_App_Engine_SDK_for_Python
* install that SDK somewhere, for example:
		su - # go to root, or maybe try 'sudo bash'
		cd /opt
		unzip ~/path_to_my_sdk/google_appengine_1.5.4.zip

Running application localy
--------------------------

* change your working directory to this git project, i.e.:

		cd gae-helloworld-py

* run development server
		/opt/google_appengine/dev_appserver.py helloworld

* point you browser to http://localhost:8080

Deploying application to remote GAE
-----------------------------------

* you need to have valid GAE Account - sign on http://code.google.com/appengine/

* you should create new Python application on your GAE Account (this is done via Web inteface)

* once application is created on GAE you may deploy it:

		/opt/google_appengine/appcfg.py update -A your_app_id helloworld

* the application should be ready on your GAE site (usually something like `http://your_app_id.appspot.com'


Live demo
---------
Is available on http://hp-hello1.appspot.com/





# Changelog


### Latest

*   .


### 0.1.0 - 27.02.2015

* Creates a config.ini if not found
* all threebot-worker relevant files are now located in `~/3bot/` or `<virtualenv>/3bot/`
* `threebot-worker` is a global available script
* Updated README


### 0.0.3 - 17.11.2014

* Raise exception only when in debug mode
* Improve package setup, install worker.py as package script
* Change location of config- and pidfile
    * primary use configfile in the root of the active virtualenv, if this fails use default configfile
    * primary create pidfile in the root of the active virtualenv, if this fails use default pidfile


### 0.0.2 - 15.10.2014

*    Catching errors for invalid configfiles


### 0.0.1 - 14.10.2014

* First release

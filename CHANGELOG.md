# Changelog


### Latest

*   .


### 0.1.5 - 04.01.2017

* Added dry run mechanism. #13


### 0.1.4 - 05.05.2016

* Bugfixes


### 0.1.3 - 05.05.2016

* Prints detailed config information


### 0.1.2 - 03.1.2015

* Fixed possible error that occurred when script contains non ascii characters


### 0.1.1 - 15.05.2015

* A wrong path was used when a configfile has to be created


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

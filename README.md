# 3bot-worker

> Configure, Build and Perform

this is the worker repo.
link to main repo.
add installation guide


# Configuration

The configuration file contains all the configuration of your 3bot installation and/or components. 
This section explains how this configuration work and which parameter are available. 

* The configuration file is located under `/etc/3bot/config.ini`.
* There is a overall `3bot-settings` section.
* It's an ini-file. 

## The `3bot-settings` section

### BOT_ENDPOINT

### LOGFILE

* That file/path must be writable by the worker.

### LOGLEVEL

* Valid values for `LOGLEVEL` could be taken from [here](https://docs.python.org/2/howto/logging.html).

### PORT

### SECRET_KEY

* Do never share your config.ini containing your `SECRET_KEY`!


## Example 

	LOGFILE = /var/log/3bot-worker.log
	LOGLEVEL = DEBUG
	



# History & Changelog

## X

Release date: 01 Sep 2014

### What's new?

* Logging
* First stable release

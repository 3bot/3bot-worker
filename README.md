# 3bot-worker

A worker is a computer program that runs as a background process on a machine. This could be a server, an embedded systems or your laptop. The worker executes the tasks of a workflow.

Jump to [3bot main repo](https://github.com/3bot/3bot/).

Use [this Gist](https://gist.github.com/walterrenner/4d8863043404bec01d0f) to install the 3bot-worker on your mashine.


## Configuration

The configuration file contains all the configuration of your 3bot installation and/or components. 
This section explains how this configuration work and which parameter are available. 

* The configuration file is located under `/etc/3bot/config.ini`.
* There is a overall `3bot-settings` section.
* It's an ini-file. 

### The `3bot-settings` section

#### BOT_ENDPOINT

#### LOGFILE

* That file/path must be writable by the worker.

#### LOGLEVEL

* Valid values for `LOGLEVEL` could be taken from [here](https://docs.python.org/2/howto/logging.html).

#### PORT

#### SECRET_KEY

* Do never share your config.ini containing your `SECRET_KEY`!


### Example 

	LOGFILE = /var/log/3bot-worker.log
	LOGLEVEL = DEBUG


## Changelog

see [CHANGELOG.md](https://github.com/3bot/3bot-worker/blob/master/CHANGELOG.md)

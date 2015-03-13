# 3bot-worker

A worker is a computer program that runs as a background process on a machine. This could be a server, an embedded systems or your laptop. The worker executes the tasks of a workflow.

Jump to [3bot main repo](https://github.com/3bot/3bot/).

## Setup/Installation

    $ pip install threebot-worker
    $ threebot-worker start



## Configuration

The configuration file contains all the configuration of your threebot-worker installation.
This section explains which parameter are available.

The configuration file is located in `~/3bot/config.ini`. If you installed 3bot in an own virtualenv it
is located in `<path to virtualenv>/3bot/config.ini`

You don't need to create a configuration file by yourself. When you first run the threebot-worker, you will be asked to enter values for the required settings.

### Available settings

#### BOT_ENDPOINT

required: True

default: *

List of hosts the worker should accept connections from (this is not well tested yet)

#### PORT

required: True

default: None

Port number the worker listens. This Port should be openend by your firewall. The port number from the 3bot application and threebot-worker settings must match.

#### SECRET_KEY

required: True

default: None

The secret key is used to establish a secure connection from the 3bot application to the threebot-worker. The secret key from the 3bot application and threebot-worker settings must match.

**Never share your your secret key!**

#### LOGFILE

required: False

default: `~/3bot/3bot.log`

Path to the logfile. theebot-worker will log all incomming connections, performed workflows and errors.

#### LOGLEVEL

required: False

default: `CRITICAL`

Valid values for `LOGLEVEL` could be taken from [here](https://docs.python.org/2/howto/logging.html).

### Example for `confing.ini`

    [3bot-settings]
    BOT_ENDPOINT = *
    PORT = 55556
    SECRET_KEY = <YOUR SECRET KEY>
	LOGFILE = /var/log/3bot-worker.log
	LOGLEVEL = DEBUG


## Changelog

see [CHANGELOG.md](https://github.com/3bot/3bot-worker/blob/master/CHANGELOG.md)

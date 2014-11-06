#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import zmq
import ConfigParser
from daemon import Daemon
import threebot_crypto
import logging

configfile = '/etc/3bot/config.ini'
_default_logfile = '/etc/3bot/3bot.log'
_default_loglevel = 'ERROR'

if os.path.isfile(configfile):
    Config = ConfigParser.ConfigParser()
    Config.read(configfile)
else:
    print "No configfile found in: '%s'" % configfile
    print "You can find a basic configfile in the Documentation."
    sys.exit(2)

FLAGS = 0

try:
    BOT = Config.get('3bot-settings', 'BOT_ENDPOINT')
    PORT = Config.get('3bot-settings', 'PORT')
except:
    print "Invalid configfile in: '%s'. Could not find BOT or PORT declaration" % configfile
    print "You can find a basic configfile in the Documentation."
    sys.exit(2)

try:
    # Read secret key - never share yours!
    SECRET_KEY = Config.get('3bot-settings', 'SECRET_KEY')
except:
    print "Invalid configfile in: '%s'. Could not find SECRET_KEY declaration" % configfile
    print "You can find a basic configfile in the Documentation."
    sys.exit(2)


try:
    LOGFILE = Config.get('3bot-settings', 'LOGFILE')
except ConfigParser.NoOptionError:
    LOGFILE = _default_logfile

try:
    _LOGLEVEL = Config.get('3bot-settings', 'LOGLEVEL', _default_loglevel)
except ConfigParser.NoOptionError:
    _LOGLEVEL = _default_loglevel

if _LOGLEVEL == 'DEBUG':
    LOGLEVEL = logging.DEBUG
elif _LOGLEVEL == 'INFO':
    LOGLEVEL = logging.INFO
elif _LOGLEVEL == 'WARNING':
    LOGLEVEL = logging.WARNING
elif _LOGLEVEL == 'ERROR':
    LOGLEVEL = logging.ERROR
else:
    LOGLEVEL = logging.CRITICAL

logging.basicConfig(filename=LOGFILE,
        level=LOGLEVEL,
        format='%(asctime)s %(message)s')

if len(sys.argv) == 2:
    if 'start' == sys.argv[1] or 'restart' == sys.argv[1]:
        print '---'
        print "Try Starting Worker with following settings found in '%s'" % configfile
        print 'ENDPOINT: %s' % str(BOT)
        print 'PORT: %s' % str(PORT)
        print 'LOGFILE: %s' % str(LOGFILE)
        print 'LOGLEVEL: %s' % str(_LOGLEVEL)
        print '---'


def writeScript(directory, script, body):
    # create and change to log directory
    task_path = os.path.join(directory, script)

    # create file
    with open(task_path, 'w+') as task_file:
        task_file.write(str(body.replace('\r\n', '\n')))
        logging.info("Saving new Script file at: %s" % task_path)

    # change permission
    os.chmod(task_path, 0755)

    return task_path


def runCommand(request):
    """
    Calls the action
    """
    response = {}
    log_id = request['workflow_log_id']
    log_time = request['workflow_log_time']
    workflow_name = request['workflow']
    foldername = "%s-%s-%s" % (log_time, str(log_id), workflow_name)
    home = os.path.expanduser("~")

    directory = os.path.join(home, '3bot', 'logs', foldername)

    if not os.path.exists(directory):
        os.makedirs(directory)

    script_bits = []

    # NOTE: keep order of hooks and task
    # TODO: cleaner implementation, not so verbose

    # add pre task hook if available
    if request.get('hooks', ) is not None:
        if request['hooks'].get('pre_task', ) is not None:
            task_filename = "pre_task_%i" % request['script']['id']
            script_bits.append(writeScript(directory, task_filename, request['hooks']['pre_task']))

    # the main task
    task_filename = "script_%i" % request['script']['id']
    task_path = os.path.join(directory, task_filename)
    task_body = request['script']['body']
    script_bits.append(writeScript(directory, task_filename, task_body))

    # add post task hook if available
    if request.get('hooks', ) is not None:
        if request['hooks'].get('post_task', ) is not None:
            task_filename = "post_task_%i" % request['script']['id']
            script_bits.append(writeScript(directory, task_filename, request['hooks']['post_task']))

    callable = ''
    if len(script_bits) > 1:
        callable = " && ".join(script_bits)
    else:
        callable = script_bits[0]

    # execute task script
    p = subprocess.Popen(callable, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    logging.info("Executing Script file at: %s" % task_path)

    ans = ""
    for line in iter(p.stdout.readline, b''):
        ans += line
    exit_code = p.wait()
    del p
    response = {'output': ans, 'exit_code': exit_code}

    return response


class WorkerDeamon(Daemon):

    def run(self):
        logging.info("Starting the 3bot worker listening on %s:%s" % (BOT, PORT))

        context = zmq.Context(1)
        server = context.socket(zmq.REP)
        logging.basicConfig(filename=LOGFILE, level=LOGLEVEL)
        server.bind("tcp://%s:%s" % (BOT, PORT))

        while True:
            request = server.recv(FLAGS)
            request = threebot_crypto.decrypt(request, SECRET_KEY)
            logging.info("Received request")
            if request:
                response = {'type': 'NOOP'}
                if 'type' in request and request['type'] == 'ACC':
                    logging.info("ACK request")
                    response = {'type': 'ACK'}
                else:
                    logging.info("Script request")
                    response = runCommand(request)
                response = threebot_crypto.encrypt(response, SECRET_KEY)
                server.send(response, flags=FLAGS)
                logging.info("Sending response")
            else:
                logging.error("Could not decrypt received message")
                if self.debug_mode:
                    raise Exception("Could not decrypt message")
            #server.send("", flags=FLAGS)


if __name__ == "__main__":
        if len(sys.argv) == 3:
            if 'start' == sys.argv[1] and 'debug' == sys.argv[2]:
                daemon = WorkerDeamon('/tmp/3bot-worker.pid', debug_mode=True)
                daemon.start()

        elif len(sys.argv) == 2:
            daemon = WorkerDeamon('/tmp/3bot-worker.pid')
            if 'start' == sys.argv[1]:
                daemon.start()
            elif 'stop' == sys.argv[1]:
                daemon.stop()
            elif 'restart' == sys.argv[1]:
                daemon.restart()
            elif 'status' == sys.argv[1]:
                daemon.status()
            else:
                print "Unknown command"
                sys.exit(2)
            sys.exit(0)
        else:
            print "usage: %s start|stop|restart|status" % sys.argv[0]
            sys.exit(2)

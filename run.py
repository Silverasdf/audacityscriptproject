#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
run.py, Ryan Peruski, 06/27/2023
This script is used to run the Audacity recording process. It sends commands to Audacity via a pipe.
The vars are defined in the config.py file. The script will record for the time specified in the config.py file then save to the save directory, also in config.py
This code is based on the template code on https://github.com/audacity/audacity/blob/master/scripts/piped-work/pipe_test.py

"""

import os
import sys
import datetime
import time
import config as CFG

if sys.platform == 'win32':
    print("pipe-test.py, running on windows")
    TONAME = '\\\\.\\pipe\\ToSrvPipe'
    FROMNAME = '\\\\.\\pipe\\FromSrvPipe'
    EOL = '\r\n\0'
else:
    print("pipe-test.py, running on linux or mac")
    TONAME = '/tmp/audacity_script_pipe.to.' + str(os.getuid())
    FROMNAME = '/tmp/audacity_script_pipe.from.' + str(os.getuid())
    EOL = '\n'

print("Write to  \"" + TONAME +"\"")
if not os.path.exists(TONAME):
    print(" ..does not exist.  Ensure Audacity is running with mod-script-pipe.")
    sys.exit()

print("Read from \"" + FROMNAME +"\"")
if not os.path.exists(FROMNAME):
    print(" ..does not exist.  Ensure Audacity is running with mod-script-pipe.")
    sys.exit()

print("-- Both pipes exist.  Good.")

TOFILE = open(TONAME, 'w')
print("-- File to write to has been opened")
FROMFILE = open(FROMNAME, 'rt')
print("-- File to read from has now been opened too\r\n")


def send_command(command):
    """Send a single command."""
    print("Send: >>> \n"+command)
    TOFILE.write(command + EOL)
    TOFILE.flush()

def get_response():
    """Return the command response."""
    result = ''
    line = ''
    while True:
        result += line
        line = FROMFILE.readline()
        if line == '\n' and len(result) > 0:
            break
    return result

def do_command(command):
    """Send one command, and return the response."""
    send_command(command)
    response = get_response()
    print("Rcvd: <<< \n" + response)
    return response

# Basically, this script sends information to a pipe that Audacity is listening to. Audacity then does the command. 
# Audacity then sends a signal back to the script, and the process repeats.
def run():
    while True:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S.%f")
        do_command("Record1stChoice")

        # Adjust the sleep time as per your requirement
        # The current value is set to 5 seconds
        time.sleep(CFG.time)

        timestamp2 = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S.%f")
        do_command("Stop")

        filename = os.path.join(CFG.save_dir, f"recording_{timestamp}to{timestamp2}.wav")
        do_command("Export2: Filename=" + filename)
        do_command("TrackClose")

run()

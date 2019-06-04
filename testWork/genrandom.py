#!/usr/bin/env python3

import sys
import pwd
import grp
import subprocess


def _init():
    _username = "user1"
    return _username


def _checkusername():
    try:
        pwd.getpwnam(_init())

    except KeyError:
        _adduser()

    else:
        print("User already exists, exiting...")
        sys.exit(1)


def _adduser():
    proc = subprocess.Popen(['useradd', '-m', _init()])
    stdout, stderr = proc.communicate()
    print("User created.")
    _getuid()


def _getuid():
    uid = pwd.getpwnam(_init()).pw_uid
    gid = grp.getgrnam(_init()).gr_gid
    print(uid, gid)


_init()
_checkusername()

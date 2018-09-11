#!/usr/bin/env python3
#   Author  : Aman Hanjrah
#   Date    : 11 Sept, 2018
#   License : GPLv3
"""
A simple Python (version 3) script (run via system cron on Unix/Linux) which checks the disk size(s) and email the admin
if size of any disks are above the threshold mentioned.
"""
import os
import shutil
import smtplib
from email.message import EmailMessage

# Define the variables, @potential user, make changes here only
_disks = ["disk1", "disk2", "disk3", "disk4", "disk5", "tools"]          # Define your disks name, without /
_threshold = "70"                                                        # Set the threshold
_path = "/tmp/diskusage.txt"                                             # Temporary path where results will be saved
_msg = EmailMessage()
_msg["From"] = "sender@example.com"                                      # sender's address
_msg["To"] = "recipient1@example.com, recipient2@example.com"            # List of recipients, separated by " , "
_msg["Subject"] = "[IMPORTANT:] One or more disks are filling up fast."  # Subject of the email
_send = smtplib.SMTP(host="smtpserver.example.com", port=25)             # Define smtp server details


def _get_size():
    _f = open(_path, "a")
    for disk in _disks:
        total, used, free = shutil.disk_usage("/" + disk)
        _percent = '%0.0f' % ((used/total) * 100)                        # Get the percentage
        if _percent > _threshold:
            _f.write("Disk space on /" + disk + "is at: " + _percent + "%\n")
    _f.close()
    email_admin()


def email_admin():
    if not os.stat(_path).st_size == 0:
        _body = open(_path, "r").read()
        _msg.set_content(_body)
        _send.send_message(_msg)
        _send.quit()
        os.remove(_path)


_get_size()

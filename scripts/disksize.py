#!/usr/bin/env python3

import os
import shutil
import smtplib
from email.message import EmailMessage

disks = ["sim1", "sim2", "sim3", "sim4", "sim5", "tools"]
_threshold = "70"
_path = "/tmp/diskusage.txt"
_msg = EmailMessage()
_msg["From"] = "aman@sim8.selfip.com"
_msg["To"] = "aman.hanjrah@kazan-networks.com, aman.hanjrah@gmail.com"
_msg["Subject"] = "[IMPORTANT:] One or more disks are filling up fast."
_send = smtplib.SMTP(host="fuji.selfip.com", port=25)


def _get_size():
    _f = open(_path, "a")
    for disk in disks:
        total, used, free = shutil.disk_usage("/" + disk)
        _percent = '%0.0f' % ((used/total) * 100)
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

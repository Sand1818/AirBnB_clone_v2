#!/usr/bin/python3
"""
Fabric script generates tgz archive fromcontents of the web_static
folder of AirBnB Clone repo.
"""
from datetime import datetime
from os.path import isdir
from fabric.api import local


def do_pack():
    """Generates a .tgz archive from contecnt of web_static folder"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        arch_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(arch_name))
        return arch_name
    except:
        return None

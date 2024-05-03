#!/usr/bin/python3
"""
 Fabric script based on 2-do_deploy_web_static.py that creates &
distributes an archive to your web servers suning deploy function
"""

from datetime import datetime
from os.path import exists, isdir
from fabric.api import env, local, put, run
env.hosts = ['54.237.106.175', '3.83.227.42']


def do_pack():
    """Generates a .tgz archive from contecnt of web_static folder"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        arch_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(arch_name))
        return arch_name
    except Exception:
        return None


def do_deploy(archive_path):
    """deploys Archive"""
    if exists(archive_path) is False:
        return False
    try:
        file_namee = archive_path.split("/")[-1]
        no_extent = file_namee.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_extent))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_namee, path, no_extent))
        run('rm /tmp/{}'.format(file_namee))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_extent))
        run('rm -rf {}{}/web_static'.format(path, no_extent))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_extent))
        return True
    except Exception:
        return False


def deploy():
    """Creates archive & uploads it to web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

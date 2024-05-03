#!/usr/bin/python3
"""
Fabric script based on 1-pack_web_static.py that distributes an
archive to the web servers sing do_deploy function
"""
from fabric.api import put, run, env
from os.path import exists
env.hosts = ['54.237.106.175', '3.83.227.42']

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
    except:
        return False

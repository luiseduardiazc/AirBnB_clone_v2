#!/usr/bin/python3
''' Compress before sending '''
from fabric.api import local, put, run, cd, env
from datetime import datetime
import os

PATH_RELEASES = '/data/web_static/releases/'
env.hosts = ['35.229.36.131', '34.74.68.170']


def do_pack():
    ''' Fabric script that generates a .tgz archive
        from the contents of the web_static
    '''
    if not os.path.isdir('./versions'):
        os.mkdir('versions')
    dateTimeObj = datetime.now()
    local('tar -cvzf versions/web_static_{}.tgz web_static'
          .format(dateTimeObj.strftime('%Y%m%d%H%M%S')))


def do_deploy(archive_path):
    '''
    function that distributes an archive to your web servers
    '''
    if not os.path.isfile(archive_path):
        return False
    put(archive_path, '/tmp/')
    with cd('/tmp'):
        file_name = archive_path.split('/')[1]
        path_to_unpack_file = PATH_RELEASES + file_name.split('.')[0]
        mkdir = 'mkdir -p {}'
        unpack_file = 'tar -xzf {} -C {}'
        run(mkdir.format(path_to_unpack_file))
        run(unpack_file.format('/tmp/' + file_name, path_to_unpack_file + '/'))
        run('rm /tmp/' + file_name)
        run('mv '+path_to_unpack_file+'/web_static/* '+path_to_unpack_file)
        run('rm -rf ' + path_to_unpack_file + '/web_static')
        path_curent = '/data/web_static/current'
        run('rm -rf ' + path_curent)
        run('ln -s ' + path_to_unpack_file + '/ ' + path_curent)
    return True

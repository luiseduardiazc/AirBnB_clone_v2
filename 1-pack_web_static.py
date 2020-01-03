#!/usr/bin/python3
''' Compress before sending '''
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    ''' Fabric script that generates a .tgz archive
        from the contents of the web_static
    '''
    if not os.path.isdir('./versions'):
        os.mkdir('versions')
    dateTimeObj = datetime.now()
    local('tar -cvzf versions/web_static_{}.tgz web_static'
          .format(dateTimeObj.strftime('%Y%m%d%H%M%S')))

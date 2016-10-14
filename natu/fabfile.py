import os
from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm

env.user = 'root'
env.hosts = ['120.25.122.107']
env.password='Q19870816q'
env.warn_only = True

# hello
def hello():
    print("hello world")

def command(cmd):
    run(cmd)

def sudo_command(cmd):
    sudo(cmd)

# upload media
def upload_media():
    run('sudo rm -r /flask/natu/media')
    put( os.getcwd() + '/media', '/flask/natu/', use_sudo=True)

def ls_media():
    run('cd /flask/natu/media')
    run('ls')
import os
from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm

env.user = 'root'
env.hosts = ['120.25.122.107']
env.password='Q19870816q'

# hello
def hello():
    print("hello world")

def command(cmd):
    run(cmd)

def sudo_command(cmd):
    sudo(cmd)

# upload media
def upload_media():
    media_dir = os.getcwd() + '/media'
    #run('sudo rm -r /flask/natu/media')

    for root,dirs,files in os.walk(media_dir):
        for name in dirs:
            print(name)

    #run('sudo mkdir /flask/natu/media')
    #put('media/test.mp4', '/flask/natu/media/',use_sudo=True)


def ls_media():
    run('cd /flask/natu/media')
    run('ls')
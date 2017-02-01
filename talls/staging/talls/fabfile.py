from fabric.api import local

def restart():
    local("sudo service uwsgi restart")
    #local("sudo service uwsgi restart")

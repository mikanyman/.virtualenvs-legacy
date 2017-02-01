#!/bin/bash

# TAMA SKRIPTI EI OLE KAYTOSSA VAAN MALLI KEHITTELYA VARTEN !!!!!!!!!!!!!!!!!!!

# Script from: http://ecarmi.org/writing/django-on-joyent/
 

# Aja ensin manuaalisesti:
# export DJANGO_SETTINGS_MODULE=/home/mnyman/.virtualenvs/churches/staging/churches/churches.settings 

#Activate the virtualenv 
#source /users/home/carmi/django_projects/mysite/bin/activate
 
PROJECT_NAME="churches" 
PROJECT_DIR="/home/mnyman/.virtualenvs/churches/staging/churches" 
PID_FILE="/home/mnyman/.virtualenvs/churches/staging/churches/churches.pid" 
SOCKET_FILE="/home/mnyman/.virtualenvs/churches/staging/churches/myproject.socket" 
BIN_PYTHON="/home/mnyman/.virtualenvs/churches/bin/python" 
DJANGO_ADMIN="/home/mnyman/.virtualenvs/churches/bin/django-admin.py" 
OPTIONS="maxchildren=2 maxspare=2 minspare=1" 
METHOD="prefork" 
 
case "$1" in
    start) 
      # Starts the Django process 
      echo "Starting Django project" 
      $BIN_PYTHON $DJANGO_ADMIN runfcgi $OPTIONS method=$METHOD socket=$SOCKET_FILE pidfile=$PID_FILE 
  ;;  
    stop) 
      # stops the daemon by cating the pidfile 
      echo "Stopping Django project" 
      kill `/bin/cat $PID_FILE` 
  ;;  
    restart) 
      ## Stop the service regardless of whether it was 
      ## running or not, start it again. 
      echo "Restarting process" 
      $0 stop
      $0 start
  ;;  
    *)  
      echo "Usage: init.sh (start|stop|restart)" 
      exit 1
  ;;  
esac 

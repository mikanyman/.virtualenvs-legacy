#!/bin/bash

# Replace these three settings.
PROJDIR="/home/mnyman/.virtualenvs/churches/staging/churches"
PIDFILE="$PROJDIR/churches.pid"
SOCKET="$PROJDIR/churches.socket"

cd $PROJDIR
if [ -f $PIDFILE ]; then
    kill `cat -- $PIDFILE`
    rm -f -- $PIDFILE
fi

export DJANGO_SETTINGS_MODULE=churches.settings # oma yritys

exec /home/mnyman/.virtualenvs/churches/bin/python manage.py \
    runfcgi method=prefork socket=$SOCKET pidfile=$PIDFILE #--settings=settings


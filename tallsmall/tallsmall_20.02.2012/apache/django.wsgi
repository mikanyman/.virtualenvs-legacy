# http://code.google.com/p/modwsgi/wiki/WhereToGetHelp?tm=6#Conference_Presentations

import os
import sys
import site

root = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, root)

activate_this = os.path.join(root, '/home/mnyman/.virtualenvs/tallsmall/bin/activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

sys.path.append('/home/mnyman/.virtualenvs/tallsmall/production') # NB
os.environ['DJANGO_SETTINGS_MODULE'] = 'tallsmall.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

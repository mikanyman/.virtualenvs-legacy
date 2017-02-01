# Lahde: http://www.foxhop.net/django-virtualenv-apache-mod_wsgi
import os
import sys

PWD = os.path.dirname(__file__)

# http://code.google.com/p/modwsgi/wiki/ApplicationIssues
# Directing any data written to standard output to standard error.
# Such data sent to standard error is then directed through the
# Apache logging system and will appear in the main Apache error log file.
sys.stdout = sys.stderr

# Add the virtual Python environment site-packages directory to the path
import site
site.addsitedir('/home/mnyman/.virtualenvs/chri/lib/python2.7/site-packages')

# http://stackoverflow.com/questions/2192323/what-is-the-python-egg-cache-python-egg-cache
# Avoid ``[Errno 13] Permission denied: '/var/www/.python-eggs'`` messages
import os
os.environ['PYTHON_EGG_CACHE'] = '/home/mnyman/.python-eggs'

#If your project is not on your PYTHONPATH by default you can add the following
if PWD.endswith('staging/chri/apache'):
    sys.path.append('/home/mnyman/.virtualenvs/chri/staging')
if PWD.endswith('production/chri/apache'):
    sys.path.append('/home/mnyman/.virtualenvs/chri/production')
os.environ['DJANGO_SETTINGS_MODULE'] = 'chri.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()


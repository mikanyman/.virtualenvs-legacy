# http://code.google.com/p/modwsgi/wiki/WhereToGetHelp?tm=6#Conference_Presentations
# http://code.google.com/p/modwsgi/wiki/ApplicationIssues#Writing_To_Standard_Output

import os
import sys
sys.stdout = sys.stderr
import site

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Based on http://code.google.com/p/modwsgi/wiki/VirtualEnvironments.
# Overlay a virtual environment on top of the baseline environment.
# Add the virtual Python environment site-packages directory to the path.

ALLDIRS = ['/home/mnyman/.virtualenvs/transdeco2.7.2+/lib/python2.7/site-packages']

# Remember original sys.path.
prev_sys_path = list(sys.path) 

# Add each new site-packages directory.
for directory in ALLDIRS:
    site.addsitedir(directory)

# Reorder sys.path so new directories at the front.
new_sys_path = [] 
for item in list(sys.path): 
    if item not in prev_sys_path: 
        new_sys_path.append(item) 
        sys.path.remove(item) 
sys.path[:0] = new_sys_path 

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Avoid "[Errno 13] Permission denied: '/var/www/.python-eggs'" messages
os.environ['PYTHON_EGG_CACHE'] = '/home/mnyman/.egg_cache'

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

sys.path.append('/home/mnyman/.virtualenvs/transdeco2.7.2+/staging')
os.environ['DJANGO_SETTINGS_MODULE'] = 'transdeco.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

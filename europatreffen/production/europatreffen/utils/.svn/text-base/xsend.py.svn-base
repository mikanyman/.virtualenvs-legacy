# http://originell.org/blog/2010/09/19/lighttpd-xsendfile/

from django.http import HttpResponse, Http404
from django.conf import settings
import os

def send(request, file=None, from_media=False):
    if not file:
        raise Http404

    #if from_media:
    #    path = os.path.join(getattr(settings, 'PROJECT_ROOT'), 'media/xsendfile', file)
    #else:
    #    path = file

    path = '/home/mnyman/.virtualenvs/tallsmall/staging/tallsmall/media/xsendfile/ET2012FI_Registration_form_PDF_auf_Deutsch.pdf'

    response = HttpResponse()
    # This makes sure that the file is downloaded and not loaded
    # into the browser's view.
    response['Content-Disposition'] = 'attachment'
    response['X-Sendfile'] = path
    return response
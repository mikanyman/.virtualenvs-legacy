from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import *

from django.http import HttpResponse
import os
import mimetypes

def index(request):
   
    dict = {
        'page_name': 'some',
        }
    return render_to_response('etreg/etreg.html', 
        dict,
        context_instance=RequestContext(request))
   
# @login_required
def xsendfile(request, file_name):
       
    # remove a trailing slash if it exists
    if file_name[-1:] == '/':
        file_name = file_name[0:-1]
    
    directory = '/home/mnyman/.virtualenvs/tallsmall/staging/tallsmall/media/xsendfile/'
    path_to_file = os.path.join(directory, file_name)
    
    #return HttpResponse(path_to_file) # debug
    
    # http://codenuts.blogspot.com/2008/10/force-download-django.html
    file = open(path_to_file,"r")
    mimetype = mimetypes.guess_type(path_to_file)[0]
    if not mimetype: mimetype = "application/octet-stream"
    response = HttpResponse(file.read(), mimetype=mimetype)
    response["Content-Disposition"]= "attachment; filename=%s" % os.path.split(path_to_file)[1]
    return response



    # http://discussion.dreamhost.com/thread-127481-post-148059.html#pid148059
    #response = HttpResponse(mimetype='application/force-download')
    #response['X-Sendfile'] = path_to_file
    #response['Content-Length'] = os.path.getsize(path_to_file)
    #response['Content-Disposition'] = 'attachment; filename="%s"' % file_name
    #return response

    #response = HttpResponse(mimetype='application/force-download')
    #response['Content-Disposition'] = 'attachment; filename=%s' % filename
    #response['X-Sendfile'] = path_to_file
    #return response

    #contract = get_object_or_404(Contract, pk=id, owner=request.user)
    #response = HttpResponse(mimetype='application/force-download')
    #response['Content-Disposition'] = 'attachment;filename="%s"' % smart_str(contract.contract_file.name)
    #response["X-Sendfile"] = "%s%s" % (settings.FILE_UPLOAD_DIR, contract.contract_file.name)
    #response['Content-length'] = contract.contract_file.size
    #return response

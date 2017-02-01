from django.shortcuts import render_to_response
from django.template import RequestContext

def show_html_page(request, html_dir, html_page):
    
    html_url = 'html/%s/%s' % (html_dir, html_page)
    context = {
        'html_url': html_url
        #'html_page': html_page
        }
    template = 'html/%s/index.html' % (html_dir,)
    
    return render_to_response(template, context, context_instance=RequestContext(request))

def old_show_html_page(request, url_status, html_page):
    
    if not html_page:
        html_page = 'index.html'

    f = open('/var/django/'+url_status+'/specs/html/mpoli/'+html_page, 'r')
    data = [line.decode('latin-1') for line in f.readlines()]
    f.close()

    return HttpResponse(data)
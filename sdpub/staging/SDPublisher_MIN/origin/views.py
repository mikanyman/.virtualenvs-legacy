#create your views here

from SDPublisher.pixelise.core import Collection
from django.shortcuts import render_to_response
#from django.http import HttpResponse

def text(request):
    p = Collection(request, 'origin')
    #return HttpResponse('OKOK')
    results = p.query("//text")
    if results.hasNext():
        text = results.next()
    else:
        return render_to_response('origin/error.html', {'message': "Can't find text element"})
    text_content = p.process_element(text, 'origin/base.py', False, None)
    return render_to_response('origin/text.html', {'page_content': text_content})

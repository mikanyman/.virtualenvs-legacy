import re

def bar():
    path_info = u'/wrk/specs/fi/tall/e0/frontpg/tuotteet/'
    #path_info = request.META['PATH_INFO']
    #path_info_mask = re.compile(r'^/(\w*)/(\w*)/(\w*)/(\w*)/(\w*)/(\w*)/.*')
    path_info_mask = re.compile(r'^/(\w*)/(\w*)/(\w*)/(\w*)/(\w*)/(\w*)/(\w*)/.*$')
    #path_info_mask = re.compile(r'^/(\w*)/(\w*)/(\w*)/(\w*)/(\w*)/(\w*)/(\w*)/.*$')
    path_info_hit = path_info_mask.match(path_info)
    
    if path_info_hit:
        status =  path_info_hit.group(1)
        project = path_info_hit.group(2)
        lang = path_info_hit.group(3)
        profile = path_info_hit.group(4)
        event = path_info_hit.group(5)
        app = path_info_hit.group(6)
        pg = path_info_hit.group(7)

        print status
    else:
        print 'aaa'
    
#bar()
def context(**kwargs):
    return kwargs['bla']

def extra():
    call_kwargs = {'bla': 'bla bla'}
    retval = context(**call_kwargs)
    print retval

extra()
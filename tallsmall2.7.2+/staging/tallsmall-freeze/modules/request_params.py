import re

def url_vars(rquest):
    
    #path_info = request.META['PATH_INFO']
    path_info = rquest.path
    path_info_mask = re.compile(r'^/(\w*)/(\w*)/(\w*)/(\w*)/(\w*)/.*$')
    path_info_hit = path_info_mask.match(path_info)

    if path_info_hit:
        lang = path_info_hit.group(1)
        profile = path_info_hit.group(2)
        event = path_info_hit.group(3)
        app = path_info_hit.group(4)
        pg = path_info_hit.group(5)
        
        return {
            'lang': lang,
            'profile': profile,
            'event': event,
            'app': app,
            'pg': pg,
        }
        
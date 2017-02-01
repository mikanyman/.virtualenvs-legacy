import re
import os

def gen_view(request):

    client_ip = request.META['REMOTE_ADDR']
    
    path_info = request.META['PATH_INFO']
    path_info_mask = re.compile(r'/(\w+)/(\w*)/.*$') # /en/detail/1/
    
    path_info_hit = path_info_mask.match(path_info)
    if path_info_hit:
        lang = path_info_hit.group(1)
        gen_view = path_info_hit.group(2)
        
        if gen_view in ['detail', 'update', 'delete']:
            page_has_object = True
        else:
            page_has_object = False
        
        return {
            'lang': lang,
            'gen_view': gen_view,
            'client_ip': client_ip,
            'page_has_object': page_has_object
            }
    else:
        # admin-toimintoja varten
        return {}
import re
import os

def gen_view(request):

    # alun /\w* lisatty django-cms varten
    
    path_info = request.META['PATH_INFO']
    path_info_mask = re.compile(r'/(\w+)/etreg/(\w*)/.*$') # /en/etreg/detail/1/
    
    path_info_hit = path_info_mask.match(path_info)
    if path_info_hit:
        lang = path_info_hit.group(1)
        gen_view = path_info_hit.group(2)
        return {
            'lang': lang,
            'gen_view': gen_view,
            }
    else:
        # admin-toimintoja varten
        return {}
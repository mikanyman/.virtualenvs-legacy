from django.utils.translation import ugettext_lazy as _

import re
import os

def cur_page(request):

    # tabs: landscapes churches rockart accounts admin
    # /(\w*) lisatty django-cms varten
    
    path_info = request.META['PATH_INFO']
    if os.name == 'nt':
        path_info_mask = re.compile(r'^/\w*/(\w*)/(\w*)/(\w*)/.*$') # project name 'maisemapaikka' included
        cur_path = path_info
    if os.name == 'posix': # tested with a199
        path_info_mask = re.compile(r'^/(\w*)/(\w*)/(\w*)/.*$') # ei muutettu
        cur_path = '/maisemapaikka%s' % (path_info,)   
    
    path_info_hit = path_info_mask.match(path_info)
    if path_info_hit:
        lang = path_info_hit.group(1)
        tab = path_info_hit.group(2)
        aspect = path_info_hit.group(3)
        
        if aspect == 'frontpg': aspect_visible_name = _('Home')
        elif aspect == 'time': aspect_visible_name = _('Travel in Time')
        elif aspect == 'photo': aspect_visible_name = _('Images')
        elif aspect == 'research': aspect_visible_name = _('Research')
        elif aspect == 'map': aspect_visible_name = _('Map')
        elif aspect == 'story': aspect_visible_name = _('Stories')
        else: aspect_visible_name = ''
    
        return {
            'cur_path': cur_path,
            'lang': lang,
            'tab': tab,
            'aspect': aspect,
            'aspect_visible_name': aspect_visible_name,
            }
    else:
        # admin-toimintoja varten, joissa ei ole kieli ym. osia
        return {}
from django.utils.translation import ugettext_lazy as _

import re
import os

def cur_page(request):

    # tabs: landscapes churches rockart accounts admin
    # /(\w*) lisatty django-cms varten
    
    path_info = request.META['PATH_INFO']
    if os.name == 'nt':
        path_info_mask = re.compile(r'^/\w+/(\w+)/(\w+)/(\w+)/.*$') # project name 'maisemapaikka' included
        cur_path = path_info
    if os.name == 'posix': # tested with a199
        
        # example path: /fi/mylocation/frontpg/
        path_info_mask = re.compile(r'^/(\w+)/(\w+)/(\w+)/.*$') # ei muutettu
        
        # example: /sv/accounts/profile/function/
        path_info_mask_accounts = re.compile(r'^/(\w+)/accounts/(\w+)/(\w+)/?$')
        
        # example: /sv/accounts/profile/
        path_info_mask_profile = re.compile(r'^/(\w+)/accounts/(\w+)/?$')
        
        cur_path = '/maisemapaikka%s' % (path_info,)

    # profile with function
    path_info_hit_accounts = path_info_mask_accounts.match(path_info)
    # profile without function
    path_info_hit_profile = path_info_mask_profile.match(path_info)
    # not accounts - other tabs
    path_info_hit = path_info_mask.match(path_info)

    # profile with function
    if path_info_hit_accounts:
        lang = path_info_hit_accounts.group(1)
        profile = path_info_hit_accounts.group(2)
        profile_func = path_info_hit_accounts.group(3)
        aspect = ''
        tab = 'accounts'
        aspect_visible_name = _('Accounts')
        cur_path = '/accounts/'
        
        return {
            'cur_path': cur_path,
            'lang': lang,
            'tab': tab,
            'aspect': aspect,
            'profile': profile,
            'profile_func': profile_func,
            'aspect_visible_name': aspect_visible_name,
            }

    # profile without function
    elif path_info_hit_profile:
        lang = path_info_hit_profile.group(1)
        
        known_funcs = ['signup', 'signin']
        if path_info_hit_profile.group(2) in known_funcs:
            profile = ''
            aspect = path_info_hit_profile.group(2)
        else:
            profile = path_info_hit_profile.group(2)
            aspect = profile
        
        profile_func = ''
        tab = 'accounts'
        aspect_visible_name = _('Accounts')
        cur_path = '/accounts/'
        
        return {
            'cur_path': cur_path,
            'lang': lang,
            'tab': tab,
            'aspect': aspect,
            'profile': profile,
            'profile_func': profile_func,
            'aspect_visible_name': aspect_visible_name,
            }

    # not accounts - other tabs
    elif path_info_hit:
        lang = path_info_hit.group(1)
        tab = path_info_hit.group(2)
        aspect = path_info_hit.group(3)
    
        
        if aspect == 'frontpg':
            aspect_visible_name = _('Home')
        elif aspect == 'time':
            aspect_visible_name = _('Travel in Time')
        elif aspect == 'photo':
            aspect_visible_name = _('Images')
        elif aspect == 'research':
            aspect_visible_name = _('Research')
        elif aspect == 'map':
            aspect_visible_name = _('Map')
        elif aspect == 'story':
            aspect_visible_name = _('Stories')
        else:
            aspect_visible_name = ''
    
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
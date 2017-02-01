import re
import os

from europatreffen.apps.etreg.models import Person

def gen_view(request):

    # alun /\w* lisatty django-cms varten
    
    email_token = request.GET.get('token', '')
    
    client_ip = request.META['REMOTE_ADDR']
    
    path_info = request.META['PATH_INFO']
    path_info_mask = re.compile(r'/(\w+)/etreg/(\w*)/.*$') # /en/etreg/detail/1/
    
    path_info_hit = path_info_mask.match(path_info)
    if path_info_hit:
        lang = path_info_hit.group(1)
        gen_view = path_info_hit.group(2)
        
        # Only allow updates from own IP
        if gen_view == 'update' or gen_view == 'detail':
            ip_test = Person.objects.filter(ip_address=client_ip)
            allowed_id_list = []
            for item in ip_test:
                allowed_id_list.append(item.id)
        else:
            ip_test = ''
            allowed_id_list = []
        
        # Bypass IP check in create-mode
        if gen_view == 'create':
            create_token = '1'
        else:
            create_token = ''
        
        return {
            'lang': lang,
            'gen_view': gen_view,
            'client_ip': client_ip,
            'allowed_id_list': allowed_id_list,
            'create_token': create_token,
            'email_token': email_token
            }
    else:
        # admin-toimintoja varten
        return {}
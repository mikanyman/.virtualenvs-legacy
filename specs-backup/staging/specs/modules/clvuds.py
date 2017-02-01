# -*- coding: UTF-8 -*-
# specs/modules/clvuds.py

from django.template.loader import get_template
from django.template import Context
from django.db.models import Q 
from specs.portal.models import Menuitem

def clvuds(url_lang, url_profile, url_event, url_app, url_pg, **kwargs):

    """ 
    kwargs: call, model, filter, template_name_part, cls, forms_dict,
            tunnistetiedot_form, jasentiedot_form, yhteystiedot_form, henk_kokotiedot_form,
            vaat_kokotiedot_form, yritystiedot_form, datatiedot_form, muut_tiedot_form
    """

    # CONTEXT FROM urls.py
    urls_context = {
        'lang': url_lang,
        'profile': url_profile,
        'event': url_event,
        'app': url_app,
        'pg': url_pg
    }
    
    # CONTEXT FROM **kwargs
    call = kwargs['call']
    model = kwargs['model']
    filter = kwargs['filter']
    template_name_part = kwargs['template_name_part']
    cls = kwargs['cls']
    
    forms_dict = {
        'tunnistetiedot_form': kwargs['tunnistetiedot_form'],
        'jasentiedot_form': kwargs['jasentiedot_form'],
        'yhteystiedot_form': kwargs['yhteystiedot_form'],
        'henk_kokotiedot_form': kwargs['henk_kokotiedot_form'],
        'vaat_kokotiedot_form': kwargs['vaat_kokotiedot_form'],
        'yritystiedot_form': kwargs['yritystiedot_form'],
        'datatiedot_form': kwargs['datatiedot_form'],
        'muut_tiedot_form': kwargs['muut_tiedot_form']
        }
    
    # MODULE
    # TO-DO
    # Ilmeni virhe: AttributeError
    # 'NoneType' object has no attribute 'lower'
    module = model.lower() + 's'
    
    # MENU
    menu_items = Menuitem.objects.filter(menu__label='clvuds')
    
    # TEMPLATE
    if template_name_part == 'clvuds':
        template_dir = 'clvuds'
    else:
        template_dir = module
        
    # CALL
    if call == 'list':
        template_function = 'list'
    else:
        template_function = 'detail'
    
    if call == 'list' or call == 'view' or call == 'update' or call == 'delete' or call == 'send' or call == 'trash':
        exec "from specs.%s.models import %s" % (module, model)
        exec "queryset = %s.objects.%s" % (model, filter)
        exec "c = Context({'%s': queryset, 'call': '%s', 'cls': '%s', 'menu_items': menu_items})" % (module, call, cls)
    elif call == 'create' or call == 'search':
        exec "c = Context({'call': '%s', 'menu_items': menu_items})" % (call,)

    c.update(urls_context)
    c.update(forms_dict)
    exec "t = get_template('%s/%s_%s.html')" % (template_dir, template_name_part, template_function)
    html = t.render(c)
    return html

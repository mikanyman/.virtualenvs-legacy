def topmenu_items(request):
    
    from specs.portal.models import Menuitem
    topmenu_items = Menuitem.objects.filter(menu__label="topnavi")
    return {'topmenu_items': topmenu_items}


def url_vars(request):
    
    try:
        site_context = request.session['site_context']
    except KeyError:
        site_context = None
        
    if site_context:
        
        if request.session['site_context'] == 'portal':
            return {
                'lang': request.session['lang'],
                'profile': request.session['profile'],
                'event': request.session['event'],
                'app': request.session['app'],
                'pg': request.session['pg'],
                'page_name': request.session['page_name'],
                'layout': request.session['layout'],
                'tab': request.session['tab'],
                'tab_name': request.session['tab_name'],
                'crumb_path': request.session['crumb_path'],
            }

        elif request.session['site_context'] == 'admin':
            return {}

        elif request.session['site_context'] == 'accounts':
            return {
                'lang': 'fi', # TO-DO: get from cookie
                'profile': 'all', # TO-DO: get from cookie
                'event': 'e0', # TO-DO: get from cookie
                'app': request.session['app'],
                'pg': request.session['pg'],
                'page_name': request.session['page_name'],
                'tab': request.session['tab'],
                'tab_name': request.session['tab_name'],
                'crumb_path': request.session['crumb_path'],
            }
            
        elif  request.session['site_context'] == 'portalaccounts':
            return {
                'lang': request.session['lang'],
                'profile': request.session['profile'],
                'event': request.session['event'],
                'app': request.session['app'],
                'pg': request.session['pg'],
                'page_name': request.session['page_name'],
                'layout': request.session['layout'],
                'tab': request.session['tab'],
                'tab_name': request.session['tab_name'],
                'crumb_path': request.session['crumb_path'],
            }

    else:
        
        """ Adminin prosessointi muodostaa erikoistapauksen """
        from specs.portal.models import Page
        #from specs.portal.models import Tab # POISTA!!!
        import re
        from django.conf import settings

        path_info = request.META['PATH_INFO']
        path_info_mask = re.compile(r'^/(\w*)/(\w*)/(\w*)/(\w*)/(\w*)/.*$')

        path_info_hit = path_info_mask.match(path_info)
    
        if path_info_hit:
            lang = path_info_hit.group(1)
            profile = path_info_hit.group(2)
            event = path_info_hit.group(3)
            app = path_info_hit.group(4)
            pg = path_info_hit.group(5)
        
            # Visible page name, visible tab name, layout
            page = Page.objects.get(application__label=app, label=pg)
            page_name = page.visible_name
            tab = page.tab
            tab_name = page.tab.visible_name
            layout = 'layouts/%s.html' % page.layout
        
            # Crumb path
            if page_name == tab_name:
                crumb_path = tab_name
            else:
                str_1 = "crumb_path = '<a href=\"/%s/%s/%s/%s/%s/\">%s</a> &rsaquo; %s'" % \
                (lang, profile, event, page.parent.application, page.parent.label, page.parent.visible_name, page_name) 
                exec str_1
                                
            request.session['django_language'] = lang
            
            return {
                'lang': lang,
                'profile': profile,
                'event': event,
                'app': app,
                'pg': pg,
                'page_name': page_name,
                'layout': layout,
                'tab': tab,
                'crumb_path': crumb_path,
            }
        else:
            # Tama lisatty adminia silmalla pitaen
            return {}
            request.session['django_language'] = 'fi' # TO-DO: poista if-testaus... ei hyva

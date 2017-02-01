# Location: modules/menus.py
# Called By: modules/PortalContext.py
# Version: 2008-08-11

from django.template.loader import get_template
from django.template import Template, Context
from specs import context_processors
from specs.portal.models import Menu, Menuitem

def render_menu(request, url_app, url_pg, menu_name, menu_type):
    
    menu_dict = {}
    submenu_dict = {} # goes in as a member in menu_dict

    exec "menu_QS = Menu.objects.get(label='%s')" % menu_name
    exec "menu_items_QS = Menuitem.objects.filter(menu__label='%s')" % menu_name

    templ = menu_QS.template
    menu_visible_name = menu_QS.visible_name
    
    if menu_type == 'main':
        menu_id = url_app
    elif menu_type == 'sub':
        #menu_id = url_pg
        menu_id = request.GET.get('class', '')

    c1 = Context(context_processors.url_vars(request)) # a dictionary
    menu_items = ''
    counter = 0
    
    # CSS 1/3
    css_items_1 = '<style type="text/css">'
    css_items_2 = ''
    css_items_3 = ''
    css_items_4 = ''
    css_items_5 = '</style>'
    
    for item in menu_items_QS:
        
        if menu_type == 'main': sel_item_name = item.application.label
        elif menu_type == 'sub': sel_item_name = item.query_string
        
        if item.query_string: exec "query_string = '?class=%s'" % item.query_string
        else: query_string = ''
        
        counter += 1
        if counter == 1:
            exec "s = '<li class=\"first\"><a href=\"/{{ lang }}/{{ profile }}/{{ event }}/%s/%s/%s\" id=\"%sLink\"><span class=\"inner\">%s</span></a></li>'" % (item.application, item.page, query_string, sel_item_name, item.visible_name)
        else:
            exec "s = '<li><a href=\"/{{ lang }}/{{ profile }}/{{ event }}/%s/%s/%s\" id=\"%sLink\"><span class=\"inner\">%s</span></a></li>'" % (item.application, item.page, query_string, sel_item_name, item.visible_name)
        t1 = Template(s)
        menu_items = menu_items + t1.render(c1)
        
        if item.submenu:
            submenu = item.submenu.label
            submenu_dict[item.label] = submenu
            
        # CSS 2/3
        exec "css_items_2 = css_items_2 + '.vmenu_sidebar#%s a#%sLink, '" % (menu_id, menu_id)
        exec "css_items_3 = css_items_3 + '.vmenu_sidebar#%s a:hover#%sLink, '" % (menu_id, menu_id)
        exec "css_items_4 = css_items_4 + '.vmenu_sidebar#%s a:hover#%sLink .inner, '" % (menu_id, menu_id)
    
    # CSS 3/3
    css_items_2 = css_items_2 + '!{color: #e54a14; background-color: #fff; border-left: solid 1px #ccc; border-right: solid 1px #ccc;}'
    css_items_2 = css_items_2.replace(', !{', ' {')
    css_items_3 = css_items_3 + '!{background-color: #dedede}'
    css_items_3 = css_items_3.replace(', !{', ' {')
    css_items_4 = css_items_4 + '!{margin-left: 1px;}'
    css_items_4 = css_items_4.replace(', !{', ' {')
    css = css_items_1 + css_items_2 + css_items_3 + css_items_4 + css_items_5

    c2 = Context({'menu_id': menu_id, 'menu_visible_name': menu_visible_name, 'menu_items': menu_items, 'css': css})
    exec "t2 = get_template('menus/%s.html')" % templ
    menu_dict['menu'] = t2.render(c2)    # HTML-rendering of menu
    menu_dict['submenu'] = submenu_dict  # dict of names of all submenus
    
    return menu_dict

def menu(request, url_app, url_pg, menu_name):
    
    menu_type = 'main'
    menu_dict = render_menu(request, url_app, url_pg, menu_name, menu_type)
    menu = menu_dict['menu']
    
    submenu = {}
    submenu_dict = menu_dict['submenu']
    for key, value in submenu_dict.iteritems():
        if submenu_dict[key]:
            menu_type = 'sub'
            submenu = render_menu(request, url_app, url_pg, submenu_dict[key], menu_type) # returns menu_dict
            menu = menu + submenu['menu']
    
    return menu
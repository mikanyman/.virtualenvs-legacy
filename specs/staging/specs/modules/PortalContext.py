# -*- coding: UTF-8 -*-
# Location: modules/PortalContext.py
# Version: 2008-08-11
# Revision history: replaced 'Entry' class with 'Feed' class

from django.template.loader import get_template
from django.template import Context, RequestContext, TemplateDoesNotExist
from specs import context_processors
from specs.portal.models import Page, Cell, Include
from specs.modules import ajankohtaista, entries, menus, namesdays, get_list, eventcal, get_object, get_blog_list # TO-DO: namesdays is not generic
#from specs.modules import clvuds # HUOM: poistettu käytosta!
#from specs.modules import menus
#from specs.modules import entries

def context(request,\
    url_lang=None, \
    url_profile=None, \
    url_event=None, \
    url_app=None, \
    url_pg=None, \
    url_id=None,\
    call=None, \
    model=None, \
    filter=None, \
    template_name_part=None, \
    cls=None,\
    tunnistetiedot_form=None, \
    jasentiedot_form=None, \
    yhteystiedot_form=None,\
    henk_kokotiedot_form=None, \
    vaat_kokotiedot_form=None, \
    yritystiedot_form=None,\
    datatiedot_form=None, \
    muut_tiedot_form=None, \
    **kwargs):

    # ========================================
    # Assign values from context_processors.py
    # ========================================
    cp_dict = context_processors.url_vars(request)
    if not url_lang and cp_dict['lang']:
        url_lang = cp_dict['lang']
    if not url_profile and cp_dict['profile']:
        url_profile = cp_dict['profile']
    if not url_event and cp_dict['event']:
        url_event = cp_dict['event']
    if not url_app and cp_dict['app']:
        url_app = cp_dict['app']
    if not url_pg and cp_dict['pg']:
        url_pg = cp_dict['pg']
    # -----------------------------------------

    feed_set = {}
    context = {}
    
    # Generate list of cells on current page
    try:
        page = Page.objects.get(application__label=url_app, label=url_pg)
        cells = page.cell_set.all() # reverse FK query. creates list of Cell-objects
    except Page.DoesNotExist:
        page = []
        cells = []

    # Create and populate feed_dict. Contains references to all objects bound to each cell on current page
    for cell in cells:
                
        # Fing background (box) for each cell
        # Populates dict 'feed_set'       
        exec "cell_%s = Cell.objects.get(application__label='%s', page__label='%s', celllocation__label='%s')" % (cell.celllocation, url_app, url_pg, cell.celllocation)
        exec "box_%s = cell_%s.box" % (cell.celllocation, cell.celllocation) 
        exec "feed_set['feed_%s'] = cell_%s.feed_set.all()" % (cell.celllocation, cell.celllocation)
        exec "feed_%s_dict = {}" % cell.celllocation
                
        counter = 0
        key = 'feed_%s' % cell.celllocation
        for f in feed_set[key]:
    
            ### user_rights
            if f.auth == True and f.confirmation == 't' and request.user.is_authenticated() and \
                request.user.is_staff and request.user.is_active:
                user_clearance = True
            elif f.auth == False and not f.confirmation:
                user_clearance = True
            else:
                user_clearance = False    

            if user_clearance:        
                counter += 1
                # initialize list:
                feed_list = []
            
                # 1. append current ENTRY to current list
                if f.entry_id: 
                    entry = entries.common_entry(f.entry_id) # ks. modules/entries.py
                                            
                    # Unescape since Django 1.0.1
                    entry = entry.replace("&quot;", "\"")
                    entry = entry.replace("&lt;", "<")
                    entry = entry.replace("&gt;", ">")
                    # this has to be last:
                    entry = entry.replace("&amp;", "&")

                    feed_list.append(entry)
                else: feed_list.append('')
                
                # 2. append APPLICATION to current list
                if f.application:
                    pass
                    """
                    clvuds_response = clvuds.clvuds(url_lang, url_profile, url_event, url_app, url_pg,\
                        call=call, model=model, filter=filter, template_name_part=template_name_part, cls=cls,\
                        tunnistetiedot_form = tunnistetiedot_form, jasentiedot_form = jasentiedot_form,\
                        yhteystiedot_form = yhteystiedot_form, henk_kokotiedot_form = henk_kokotiedot_form,\
                        vaat_kokotiedot_form = vaat_kokotiedot_form, yritystiedot_form = yritystiedot_form,\
                        datatiedot_form = datatiedot_form, muut_tiedot_form = muut_tiedot_form)
                    feed_list.append(clvuds_response)
                    """
                else: feed_list.append('')
                
                # 3. append current INCLUDE to current list
                """ gets context from extra_context and context_processor """
                if f.include:
                    if kwargs:
                        extra_context = {}
                        for k, v in kwargs.iteritems():
                           #exec "extra_context.update({'%s': '%s'})" % (k, v)
                           extra_context.update({k: v})
                    else:
                        extra_context = {}
                    c = Context(extra_context)
                    # add to context from context_processor
                    c.update(context_processors.url_vars(request))
                    i = Include.objects.get(id=f.include_id)
                    try:
                        t = get_template(i.path)
                        feed_list.append(t.render(c))
                    except TemplateDoesNotExist:
                        feed_list.append('')
                else: feed_list.append('')
            
                # 4. append current CALLABLE with template to current list
                if f.callable:
                    try:
                        """
                        Option 1: has template
                        NOTE use of RequestContext!
                        """
                        t = get_template(f.callable.template)
                        try:
                            exec "c = RequestContext(request, { 'content_from_callable': %s }, processors=[context_processors.url_vars])" % f.callable.call
                            feed_list.append(t.render(c))
                        except AttributeError:
                            feed_list.append('AttributeError: type object \'list\' has no attribute \'list\'')
                        except SyntaxError:
                            feed_list.append('SyntaxError: Template Only. Add Callable or Remove Callable from Feed')
                        except UnboundLocalError:
                            feed_list.append('UnboundLocalError: Missing Argument')
                    except TemplateDoesNotExist:
                        """ Option 2: does not have template """
                        """ Option 3: use this in case of list and for-loop """
                        exec "feed_list.append(%s)" % f.callable.call
                else: feed_list.append('')
                
                #5. append MENU to current list
                if f.menu_id:
                    exec "menu = menus.menu(request, url_app, url_pg, '%s')" % f.menu
                    feed_list.append(menu)
                else: feed_list.append('')
                                                
                # insert current list into dict
                exec "feed_%s_dict['%s'] = %s" % (cell.celllocation, counter, feed_list)
              
        # Create context
        exec "context['cell_template_%s'] = 'boxes/%s.html'" % (cell.celllocation, cell.box)
        exec "context['feed_%s_dict'] = feed_%s_dict" % (cell.celllocation, cell.celllocation)
             
    return context
        
# Location: modules/PortalContext.py
# Version: 2008-08-07
# Revision history: 'append current include to current list', line 69 f.

from django.template.loader import get_template
from django.template import Context, TemplateDoesNotExist
from specs.portal.models import Page, Cell, Include
from specs.modules import namesdays # TO-DO: This is not generic
from specs import context_processors

def context(request, url_app, url_pg):
    
    entry_set = {}
    context = {}
    
    # Generate list of cells on current page
    try:
        page = Page.objects.get(application__name=url_app, name=url_pg)
        layout_file = 'layouts/%s.html' % page.layout
        cells = page.cell_set.all() # reverse FK query. creates list of Cell-objects
    except Page.DoesNotExist:
        page = []
        cells = []
        layout_file = 'layouts/3col.html' # TO-DO: Mit‰ k‰ytet‰‰n kun sivua ei ole tiedossa?

    # Create and populate entry_dict. Contains references to all objects bound to each cell on current page
    cell_counter = 0 # DEL AFTER DEBUG
    for cell in cells:
        
        cell_counter += 1 # DEL AFTER DEBUG
        
        # Fing background (box) for each cell
        # Populates dict 'entry_set'       
        str_1 = "cell_%s = Cell.objects.get(application__name='%s', page__name='%s', celllocation__name='%s')" % (cell.celllocation, url_app, url_pg, cell.celllocation)
        str_2 = "box_%s = cell_%s.box" % (cell.celllocation, cell.celllocation) 
        str_3 = "entry_set['entry_%s'] = cell_%s.entry_set.all()" % (cell.celllocation, cell.celllocation)
        str_4 = "entry_%s_dict = {}" % cell.celllocation
        
        exec str_1
        exec str_2        
        exec str_3
        exec str_4
        
        counter = 0
        key = 'entry_%s' % cell.celllocation
        for e in entry_set[key]: 
    
            ### user_rights
            if e.auth == True and e.confirmation == 't' and request.user.is_authenticated() and \
                request.user.is_staff and request.user.is_active:
                user_clearance = True
            elif e.auth == False and not e.confirmation:
                user_clearance = True
            else:
                user_clearance = False    

            if user_clearance:        
                counter += 1
                # initialize list:
                entry_list_name = []
            
                # 1. append current title to current list
                if e.title: entry_list_name.append('<strong>'+e.title+'</strong><br />')
                else: entry_list_name.append('')
            
                # 2. append current body to current list
                if e.body: entry_list_name.append(e.body)
                else: entry_list_name.append('')

                # 3. append current include to current list
                if e.include:
                    c = context_processors.url_vars(request)
                    i = Include.objects.get(id=e.include_id)
                    try:
                        t = get_template(i.path)
                        entry_list_name.append(t.render(c))
                    except TemplateDoesNotExist:
                        entry_list_name.append('')
                else: entry_list_name.append('')
            
                # 4. append current callable with template to current list
                if e.callable:
                    try:
                        t = get_template(e.callable.template)
                        try:
                            c = Context({ 'content_from_callable': eval(str(e.callable.call)) })
                            entry_list_name.append(t.render(c))
                        except SyntaxError:
                            entry_list_name.append('SyntaxError: Template Only. Add Callable or Remove Callable from Entry')
                        except UnboundLocalError:
                            entry_list_name.append('UnboundLocalError: Missing Argument')
                    except TemplateDoesNotExist:
                        entry_list_name.append(eval(str(e.callable.call)))
                else: entry_list_name.append('')
              
                # insert current list into dict
                str_5 = "entry_%s_dict['%s'] = %s" % (cell.celllocation, counter, entry_list_name)
                exec str_5
              
        # Create context
        str_6 = "context['cell_template_%s'] = 'boxes/%s.html'" % (cell.celllocation, cell.box)
        str_7 = "context['entry_%s_dict'] = entry_%s_dict" % (cell.celllocation, cell.celllocation)
     
        exec str_6
        exec str_7
        
    context['layout'] = layout_file
    return context
        
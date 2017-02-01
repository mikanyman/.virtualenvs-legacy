from specs.portal.models import Cell

def entry_sets(url_app, url_pg):
    
    # Many-to-Many relations. entry_set corresponds to related_name

    entry_set = {}

    ### COL 1
    # Get ResultSet objects from Entry-table using cell as search key
    try:
        cell_1_1 = Cell.objects.get(application__name='%s', page__name='%s', celllocation__name='1_1') % (url_app, url_pg)
        entry_set['entry_1_1'] = cell_1_1.entry_set.all()
    except Cell.DoesNotExist:
        entry_set['entry_1_1'] = ''
        
    try:
        cell_1_2 = Cell.objects.get(application__name='%s', page__name='%s', celllocation__name='1_2') % (url_app, url_pg)
        entry_set['entry_1_2'] = cell_1_2.entry_set.all()
    except Cell.DoesNotExist:
        entry_set['entry_1_2'] = ''
        
    try:
        cell_1_3 = Cell.objects.get(application__name='%s', page__name='%s', celllocation__name='1_3') % (url_app, url_pg)
        entry_set['entry_1_3'] = cell_1_3.entry_set.all()
    except Cell.DoesNotExist:
        entry_set['entry_1_3'] = ''
        
    try:
        cell_1_4 = Cell.objects.get(application__name='%s', page__name='%s', celllocation__name='1_4') % (url_app, url_pg)
        entry_set['entry_1_4'] = cell_1_4.entry_set.all()
    except Cell.DoesNotExist:
        entry_set['entry_1_4'] = ''
        
    try:
        cell_1_5 = Cell.objects.get(application__name='%s', page__name='%s', celllocation__name='1_5') % (url_app, url_pg)
        entry_set['entry_1_5'] = cell_1_5.entry_set.all()
    except Cell.DoesNotExist:
        entry_set['entry_1_5'] = ''

    ### COL 2
    try:
        cell_2_1 = Cell.objects.get(application__name='%s', page__name='%s', celllocation__name='2_1') % (url_app, url_pg)
        entry_set['entry_2_1'] = cell_2_1.entry_set.all()
    except Cell.DoesNotExist:
        entry_set['entry_2_1'] = ''
        
    try:
        cell_2_2 = Cell.objects.get(application__name='%s', page__name='%s', celllocation__name='2_2') % (url_app, url_pg)
        entry_set['entry_2_2'] = cell_2_2.entry_set.all()
    except Cell.DoesNotExist:
        entry_set['entry_2_2'] = ''
        
    try:
        cell_2_3 = Cell.objects.get(application__name='%s', page__name='%s', celllocation__name='2_3') % (url_app, url_pg)
        entry_set['entry_2_3'] = cell_2_3.entry_set.all()
    except Cell.DoesNotExist:
        entry_set['entry_2_3'] = ''
        
    try:
        cell_2_4 = Cell.objects.get(application__name='%s', page__name='%s', celllocation__name='2_4') % (url_app, url_pg)
        entry_set['entry_2_4'] = cell_2_4.entry_set.all()
    except Cell.DoesNotExist:
        entry_set['entry_2_4'] = ''
        
    try:
        cell_2_5 = Cell.objects.get(application__name='%s', page__name='%s', celllocation__name='2_5') % (url_app, url_pg)
        entry_set['entry_2_5'] = cell_2_5.entry_set.all()
    except Cell.DoesNotExist:
        entry_set['entry_2_5'] = ''
    
    ### COL 3
    try:
        cell_3_1 = Cell.objects.get(application__name='%s', page__name='%s', celllocation__name='3_1') % (url_app, url_pg)
        entry_set['entry_3_1'] = cell_3_1.entry_set.all()
    except Cell.DoesNotExist:
        entry_set['entry_3_1'] = ''
        
    try:
        cell_3_2 = Cell.objects.get(application__name='%s', page__name='%s', celllocation__name='3_2') % (url_app, url_pg)
        entry_set['entry_3_2'] = cell_3_2.entry_set.all()
    except Cell.DoesNotExist:
        entry_set['entry_3_2'] = ''
        
    try:
        cell_3_3 = Cell.objects.get(application__name='%s', page__name='%s', celllocation__name='3_3') % (url_app, url_pg)
        entry_set['entry_3_3'] = cell_3_3.entry_set.all()
    except Cell.DoesNotExist:
        entry_set['entry_3_3'] = ''
        
    try:
        cell_3_4 = Cell.objects.get(application__name='%s', page__name='%s', celllocation__name='3_4') % (url_app, url_pg)
        entry_set['entry_3_4'] = cell_3_4.entry_set.all()
    except Cell.DoesNotExist:
        entry_set['entry_3_4'] = ''
        
    try:
        cell_3_5 = Cell.objects.get(application__name='%s', page__name='%s', celllocation__name='3_5') % (url_app, url_pg)
        entry_set['entry_3_5'] = cell_3_5.entry_set.all()
    except Cell.DoesNotExist:
        entry_set['entry_3_5'] = ''
    
    return entry_set

def cell_contexts(url_pg):
    
    ### Mainly about which box to use in template. This is declared in class Cell
    
    cell_context = {}

    ### COL 1
    # Get single lines from Cell-table
    try:
        cell_1_1 = Cell.objects.get(application__name='%s', page__name='%s', celllocation__name='1_1') % (url_app, url_pg)
        cell_context['cell_1_1'] = cell_1_1
    except Cell.DoesNotExist:
        cell_context['cell_1_1'] = ''
        
    try:
        cell_1_2 = Cell.objects.get(application__name='%s', page__name='%s', celllocation__name='1_2') % (url_app, url_pg)
        cell_context['cell_1_2'] = cell_1_2
    except Cell.DoesNotExist:
        cell_context['cell_1_2'] = ''
        
    try:
        cell_1_3 = Cell.objects.get(application__name='%s', page__name='%s', celllocation__name='1_3') % (url_app, url_pg)
        cell_context['cell_1_3'] = cell_1_3
    except Cell.DoesNotExist:
        cell_context['cell_1_3'] = ''
        
    try:
        cell_1_4 = Cell.objects.get(application__name='%s', page__name='%s', celllocation__name='1_4') % (url_app, url_pg)
        cell_context['cell_1_4'] = cell_1_4
    except Cell.DoesNotExist:
        cell_context['cell_1_4'] = ''
        
    try:
        cell_1_5 = Cell.objects.get(application__name='%s', page__name='%s', celllocation__name='1_5') % (url_app, url_pg)
        cell_context['cell_1_5'] = cell_1_5
    except Cell.DoesNotExist:
        cell_context['cell_1_5'] = ''
        
    ### COL 2
    try:
        cell_2_1 = Cell.objects.get(application__name='%s', page__name='%s', celllocation__name='2_1') % (url_app, url_pg)
        cell_context['cell_2_1'] = cell_2_1
    except Cell.DoesNotExist:
        cell_context['cell_2_1'] = ''
        
    try:
        cell_2_2 = Cell.objects.get(application__name='%s', page__name='%s', celllocation__name='2_2') % (url_app, url_pg)
        cell_context['cell_2_2'] = cell_2_2
    except Cell.DoesNotExist:
        cell_context['cell_2_2'] = ''
        
    try:
        cell_2_3 = Cell.objects.get(application__name='%s', page__name='%s', celllocation__name='2_3') % (url_app, url_pg)
        cell_context['cell_2_3'] = cell_2_3
    except Cell.DoesNotExist:
        cell_context['cell_2_3'] = ''
        
    try:
        cell_2_4 = Cell.objects.get(application__name='%s', page__name='%s', celllocation__name='2_4') % (url_app, url_pg)
        cell_context['cell_2_4'] = cell_2_4
    except Cell.DoesNotExist:
        cell_context['cell_2_4'] = ''
        
    try:
        cell_2_5 = Cell.objects.get(application__name='%s', page__name='%s', celllocation__name='2_5') % (url_app, url_pg)
        cell_context['cell_2_5'] = cell_2_5
    except Cell.DoesNotExist:
        cell_context['cell_2_5'] = ''
        
    ### COL 3
    try:
        cell_3_1 = Cell.objects.get(application__name='%s', page__name='%s', celllocation__name='3_1') % (url_app, url_pg)
        cell_context['cell_3_1'] = cell_3_1
    except Cell.DoesNotExist:
        cell_context['cell_3_1'] = ''
        
    try:
        cell_3_2 = Cell.objects.get(application__name='%s', page__name='%s', celllocation__name='3_2') % (url_app, url_pg)
        cell_context['cell_3_2'] = cell_3_2
    except Cell.DoesNotExist:
        cell_context['cell_3_2'] = ''
        
    try:
        cell_3_3 = Cell.objects.get(application__name='%s', page__name='%s', celllocation__name='3_3') % (url_app, url_pg)
        cell_context['cell_3_3'] = cell_3_3
    except Cell.DoesNotExist:
        cell_context['cell_3_3'] = ''
        
    try:
        cell_3_4 = Cell.objects.get(application__name='%s', page__name='%s', celllocation__name='3_4') % (url_app, url_pg)
        cell_context['cell_3_4'] = cell_3_4
    except Cell.DoesNotExist:
        cell_context['cell_3_4'] = ''
        
    try:
        cell_3_5 = Cell.objects.get(application__name='%s', page__name='%s', celllocation__name='3_5') % (url_app, url_pg)
        cell_context['cell_3_5'] = cell_3_5
    except Cell.DoesNotExist:
        cell_context['cell_3_5'] = ''

    return cell_context
    
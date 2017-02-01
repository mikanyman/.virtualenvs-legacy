# specs/modules/list.py
# forms a pair with get_object.py - both take params from the URL

from django.db.models import Q
from specs.portal.models import Entry

def list_category(category):
    """
    Lists published entries (class Entry) on a page (class Page)
    Template determined by portal.Callable; common/list_published.html
    """
    query = Q(entrystatus='published') & Q(categories__label=category)
    queryset = Entry.objects.filter(query).order_by('-created')
    return queryset

def list_published(url_pg):
    """
    Lists published entries (class Entry) on a page (class Page)
    Template determined by portal.Callable; common/list_published.html
    """
    query = Q(entrystatus='published') & Q(categories__pages__label=url_pg)
    queryset = Entry.objects.filter(query).order_by('-created')
    return queryset

def list_latest():
    """
    Lists latest entries (class Entry) on a page (class Page)
    Template determined by portal.Callable; common/list_latest.html
    """
    query = Q(entrystatus='published') & Q(list_latest=True)
    queryset = Entry.objects.filter(query).order_by('-created')[:10]
    return queryset

def list_blogs_for_author(request):
    """
    List all blogs for current author
    Template determined by portal.Callable; common/list_blogs_for_author.html
    http://stackoverflow.com/questions/928264/in-django-how-do-you-retrieve-a-field-of-a-many-to-many-related-class
    """
    
    blog = request.GET.get('blog', '')
    if blog:
        query = Q(entrystatus='published') & Q(categories__label=blog)
        queryset = Entry.objects.filter(query).order_by('created')
        return queryset
    else:
        # Find entry_id based on query string, eg. '105'
        import re
        path_info = request.META['PATH_INFO']
        path_info_mask = re.compile(r'^/\w*/\w*/\w*/\w*/\w*/(\w*)/$') # blog url with ID
        path_info_hit = path_info_mask.match(path_info)
        if path_info_hit:
            entry_id = path_info_hit.group(1)

        # Find category for given entry_id
        # Blogs are coded as categories in Entries, eg. kallen_blogi, erika etc. (not ideal...)
        cur_category = Entry.objects.filter(id__exact=entry_id)[0].categories.all()[0]
        
        # Find entries corresponding to given category
        exec "query = Q(entrystatus='published') & Q(categories__label='%s')" % (cur_category,)
        queryset = Entry.objects.filter(query).order_by('created')
        return queryset

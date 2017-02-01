# specs/blog/views.py

from django.views.generic.list_detail import object_list, object_detail
from django.db.models import Q

from specs.portal.models import Entry
from specs.modules import PortalContext

def list_entries(request, url_lang, url_profile, url_event, url_app, url_pg):

    blog = request.GET.get('blog', '')
    context = PortalContext.context(request, url_lang, url_profile, url_event, url_app, url_pg)
    ## GENERIC VIEWS
    ## generic views use RequestContext by default
    ## TO-DO: generic views voitaisiin siirtaa PortalContext.py moduliin
    query = Q(entrystatus='published') & Q(categories__label=blog)
    return object_list(request,
        queryset = Entry.objects.filter(query).order_by('-created'),
        paginate_by = 10,
        template_name = 'blog/blog_list.html',
        extra_context = context
    )

def detail(request, url_lang, url_profile, url_event, url_app, url_pg, url_id):

    ## GENERIC VIEWS
    blog = request.GET.get('blog', '')
    context = PortalContext.context(request, url_lang, url_profile, url_event, url_app, url_pg, url_id)
    return object_detail(request,
        queryset = Entry.objects.all(),
        object_id = url_id,
        template_name = 'blog/blog_detail.html',
        extra_context = context
    )

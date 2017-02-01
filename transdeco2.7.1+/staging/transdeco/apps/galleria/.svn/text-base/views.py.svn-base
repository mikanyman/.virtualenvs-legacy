from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic.list_detail import object_list, object_detail
from django.db.models import Q

from transdeco.apps.galleria.models import Site, Artist, Work
from transdeco.apps.flatpages.models import Flatpage
from transdeco import settings

def increment_counter(request):
            session_id
            ip_number = request.META['REMOTE_ADDR']
            created
            created = datetime.datetime.today()

def frontpage(request, **kwargs):
    """ generic view for frontpage """
        
    pg = kwargs['pg']
    site = Site.objects.all()
        
    context = {
        'referer': request.META.get('HTTP_REFERER', ''),
        'session': request.session.session_key,
        'site': site,
        'pg': pg,
        }

    return object_list(request,
        queryset = Artist.objects.filter(act_pass__exact="A"),
        template_name = 'frontpage_list.html',
        extra_context=context
        )

def artist_page(request, **kwargs):
    """ generic view for artist page """

    pg = kwargs['pg']
    artist_label = kwargs['artist_label']
    
    artist = Artist.objects.get(label=artist_label)
    #query = 
    works = Work.objects.filter(artist__person_name=artist.person_name, items_in_store__gt=0)
    image_dict = {}
    
    for work in works:
        # reverse; image_set is a manager...
        exec "image_dict[work.item_number] = work.image_set.filter(work__item_number='%d')" % (work.item_number)
 
    context = {
        'pg': pg,
        'artist': artist,
        'works': works,
        'image_dict': image_dict
        }
    
    ## List of artists
    return object_list(request,
        queryset = Artist.objects.filter(act_pass__exact="A"),
        template_name = 'artist_list.html',
        extra_context=context
        )
    
def work_page(request, **kwargs):
    
    pg = kwargs['pg']
    work_id = kwargs['work_id']
    artist_label = kwargs['artist_label']
    
    artist = Artist.objects.get(label=artist_label)
    work = Work.objects.get(item_number=work_id)
    exec "image = work.image_set.get(work__item_number='%s')" % work_id

    context = {
        'pg': pg,
        'artist': artist,
        'work': work,
        'image': image
        }    
    
    ## List of artists
    return object_list(request,
        queryset = Artist.objects.filter(act_pass__exact="A"),
        template_name = 'work_page.html',
        extra_context=context
        )

def flatpage(request, **kwargs):
    
    site = Site.objects.all()
    
    pg = kwargs['pg']

    flatpage_url = '/%s/' % pg
    flatpage = Flatpage.objects.get(url=flatpage_url)
    t = loader.get_template('flatpage.html')
    c = Context({
        'pg': pg,
        'site': site,
        'flatpage': flatpage,
        'STATIC_URL': settings.STATIC_URL
    })
    return HttpResponse(t.render(c))


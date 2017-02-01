# transdeco/galleria/urls.py

from django.conf.urls.defaults import *

urlpatterns = patterns('transdeco.galleria.views',
    url(r'(?P<pg>taiteilijat)/(?P<artist_label>\w+)/$', 'artist_page'),
    url(r'(?P<pg>teos)/(?P<artist_label>\w+)/(?P<work_id>\w+)/$', 'work_page'),
    url(r'(?P<pg>yhteys)/$', 'flatpage'),
    url(r'(?P<pg>tilaus)/$', 'flatpage'),
    url(r'(?P<pg>\w+)/$', 'frontpage'),
    url(r'$', 'frontpage', {'pg': 'aloitus'}),
)

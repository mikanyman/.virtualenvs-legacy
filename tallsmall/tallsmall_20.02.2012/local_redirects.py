from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to

# ---------- redirects ----------
REDIRECTS = patterns('',
    #url(r'^$', redirect_to, {'url': 'http://europatreffen.tallsmall.fi/en/etreg/create/'}),
    #url(r'^en/$', redirect_to, {'url': 'http://europatreffen.tallsmall.fi/en/etreg/create/'}),
    #url(r'^fi/$', redirect_to, {'url': 'http://europatreffen.tallsmall.fi/fi/etreg/create/'}),
    #url(r'^de/$', redirect_to, {'url': 'http://europatreffen.tallsmall.fi/de/etreg/create/'}),
    url(r'^etreg/$', redirect_to, {'url': 'http://europatreffen.tallsmall.fi/en/etreg/create/'}),
    url(r'^fi/etreg/$', redirect_to, {'url': 'http://europatreffen.tallsmall.fi/fi/etreg/create/'}),
    url(r'^en/etreg/$', redirect_to, {'url': 'http://europatreffen.tallsmall.fi/en/etreg/create/'}),
    url(r'^de/etreg/$', redirect_to, {'url': 'http://europatreffen.tallsmall.fi/de/etreg/create/'}),
)


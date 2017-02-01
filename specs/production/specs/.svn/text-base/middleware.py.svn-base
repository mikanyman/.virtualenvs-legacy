from django.http import HttpResponsePermanentRedirect
from django.conf import settings
from specs.portal.models import Page
from specs.portal.models import Tab
import re
        
class SetUserSession(object):
    
    def process_request(self, request):
        
        path_info = request.META['PATH_INFO']
        
        path_info_mask_portal = re.compile(r'^/(\w*)/(\w*)/(\w*)/(\w*)/(\w*)/.*$')
        path_info_mask_admin = re.compile(r'^/admin/.*$')
        path_info_mask_accounts = re.compile(r'^/accounts/(.*)/.*$') # .* for page names like 'password/reset'
        path_info_mask_portalaccounts = re.compile(r'^/(\w*)/(\w*)/(\w*)/accounts/(.*)/.*$') # .* for page names like 'password/reset'
        
        path_info_hit_portal = path_info_mask_portal.match(path_info)
        path_info_hit_admin = path_info_mask_admin.match(path_info)
        path_info_hit_accounts = path_info_mask_accounts.match(path_info)
        path_info_hit_portalaccounts = path_info_mask_portalaccounts.match(path_info)
    
        if path_info_hit_portal:
            
            ### Set site_context
            request.session['site_context'] = 'portal'

            ### Path info
            lang = path_info_hit_portal.group(1)
            profile = path_info_hit_portal.group(2)
            event = path_info_hit_portal.group(3)
            app = path_info_hit_portal.group(4)
            pg = path_info_hit_portal.group(5)
            
            ### Visible page name, visible tab name, layout
            page = Page.objects.get(application__label=app, label=pg)
            page_name = page.visible_name
            tab = page.tab
            tab_name = page.tab.visible_name
            layout = 'layouts/%s.html' % page.layout

            ### Crumb path
            if page_name == tab_name:
                request.session['crumb_path'] = tab_name
            else:
                str_1 = "request.session['crumb_path'] = '<a href=\"/%s/%s/%s/%s/%s/\">%s</a> &rsaquo; %s'" % \
                (lang, profile, event, page.parent.application, page.parent.label, page.parent.visible_name, page_name) 
                exec str_1
            
            ### Set Session
            request.session['lang'] = lang
            request.session['profile'] = profile
            request.session['event'] = event
            request.session['app'] = app
            request.session['pg'] = pg
            #request.session['page'] = page
            request.session['page_name'] = page_name
            request.session['tab'] = tab
            request.session['tab_name'] = tab_name 
            request.session['layout'] = layout        
            request.session['django_language'] = lang

        elif path_info_hit_admin:
            
            ### Set site_context
            request.session['site_context'] = 'admin'
            
        elif path_info_hit_accounts:
            
            ### Set site_context
            request.session['site_context'] = 'accounts'

            ### Path info
            lang = 'fi' # TO-DO: get from cookie
            profile = 'all' # TO-DO: get from cookie
            event = 'e0' # TO-DO: get from cookie
            app = 'accounts'
            pg = path_info_hit_accounts.group(1)
            
            ### Visible page name, visible tab name, layout
            page = Page.objects.get(application__label=app, label=pg)
            page_name = page.visible_name
            tab = page.tab
            tab_name = page.tab.visible_name
            layout = 'layouts/%s.html' % page.layout
            
            ### Crumb path
            if page_name == tab_name:
                request.session['crumb_path'] = tab_name
            else:
                str_1 = "request.session['crumb_path'] = '<a href=\"/%s/%s/%s/%s/%s/\">%s</a> &rsaquo; %s'" % \
                (lang, profile, event, page.parent.application, page.parent.label, page.parent.visible_name, page_name) 
                exec str_1
            
            ### Set Session
            request.session['app'] = app
            request.session['pg'] = pg
            request.session['page_name'] = page_name
            request.session['tab'] = tab
            request.session['tab_name'] = tab_name     
            request.session['django_language'] = 'fi' # TO-DO: make dynamic...
            
        elif path_info_hit_portalaccounts:
            
            ### Set site_context
            request.session['site_context'] = 'portalaccounts'

            ### Path info
            lang = path_info_hit_portal.group(1)
            profile = path_info_hit_portal.group(2)
            event = path_info_hit_portal.group(3)
            app = 'accounts'
            pg = path_info_hit_accounts.group(4)
            
            ### Visible page name, visible tab name, layout
            page = Page.objects.get(application__label=app, label=pg)
            page_name = page.visible_name
            tab = page.tab
            tab_name = page.tab.visible_name
            layout = 'layouts/%s.html' % page.layout
            
            ### Crumb path
            if page_name == tab_name:
                request.session['crumb_path'] = tab_name
            else:
                str_1 = "request.session['crumb_path'] = '<a href=\"/%s/%s/%s/accounts/%s/\">%s</a> &rsaquo; %s'" % \
                (lang, profile, event, page.parent.application, page.parent.label, page.parent.visible_name, page_name) 
                exec str_1
            
            ### Set Session
            request.session['app'] = app
            request.session['pg'] = pg
            request.session['page_name'] = page_name
            request.session['tab'] = tab
            request.session['tab_name'] = tab_name     
            request.session['django_language'] = lang

        else:
            pass
            
            
class SetLangFi(object):
    def process_request(self, request):
        request.session['django_language'] = 'fi'

class UrlRedirectMiddleware:
    """
    SOURCE: http://www.djangosnippets.org/snippets/510/
    
    This middleware lets you match a specific url and redirect the request to a
    new url.

    You keep a tuple of url regex pattern/url redirect tuples on your site
    settings, example:

    URL_REDIRECTS = (
        (r'www\.example\.com/hello/$', 'http://hello.example.com/'),
        (r'www\.example2\.com/$', 'http://www.example.com/example2/'),
    )

    """    
    def process_request(self, request):
        host = request.META['HTTP_HOST'] + request.META['PATH_INFO']
        for url_pattern, redirect_url in settings.URL_REDIRECTS:
            regex = re.compile(url_pattern)
            if regex.match(host):
                return HttpResponsePermanentRedirect(redirect_url)


## maisemapaikka/apps/wiki/admin.py

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from maisemapaikka.apps.wiki.models import RemoteHtml, Tab, Creator # Page

#class PageAdmin(admin.ModelAdmin):
#    list_display = ('link_header',)

    # http://blog.ifabio.com/2010/02/22/django-filebrowser-tinymce-%E2%80%93-grappelli-made-easy/
    #class Media:
    #    js = ('/static/tiny_mce/tiny_mce_src.js', '/static/filebrowser/js/tinymceadmin.js')
    
class RemoteHtmlAdmin(admin.ModelAdmin):
    list_display = ('link_header', 'creator', 'tab', 'url')
    
class TabAdmin(admin.ModelAdmin):
    list_display = ('visiblename', 'tabname')
    
class CreatorAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname')
    
#admin.site.register(Page, PageAdmin)
admin.site.register(RemoteHtml, RemoteHtmlAdmin)
admin.site.register(Tab, TabAdmin)
admin.site.register(Creator, CreatorAdmin)
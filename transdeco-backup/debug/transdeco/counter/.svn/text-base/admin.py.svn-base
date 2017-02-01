## transdeco/counter/admin.py

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _ 
from transdeco.counter.models import ViewCount, PathCount


class PathCountAdmin(admin.ModelAdmin):
    list_display = ('path',)
    
class ViewCountAdmin(admin.ModelAdmin):
    list_display = ('url', 'count')
    ordering = ('url',)
    
admin.site.register(PathCount, PathCountAdmin)
admin.site.register(ViewCount, ViewCountAdmin)
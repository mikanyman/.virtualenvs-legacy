## specs/tagforum/admin.py

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _ 
from specs.tagforum.models import Entry

class EntryAdmin(admin.ModelAdmin):
    list_display = ('username', 'tag_list')
    list_filter = ['username']
    search_fields = ['username']

admin.site.register(Entry, EntryAdmin)
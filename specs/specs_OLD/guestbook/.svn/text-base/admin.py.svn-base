from django.contrib import admin
from specs.guestbook.models import Entry

class EntryAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_created')
    
admin.site.register(Entry, EntryAdmin)
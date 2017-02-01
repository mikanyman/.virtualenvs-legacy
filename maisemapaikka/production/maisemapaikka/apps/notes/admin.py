## maisemapaikka/apps/notes/admin.py

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from maisemapaikka.apps.notes.models import Note
    
class NoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'pub_date', 'title', 'body')

admin.site.register(Note, NoteAdmin)


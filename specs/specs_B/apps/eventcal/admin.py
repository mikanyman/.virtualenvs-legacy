## specs/apps/eventcal/admin.py

from django.contrib import admin
from specs.apps.eventcal.models import Event, Eventdate

class EventAdmin(admin.ModelAdmin):
    list_display = ('theme', 'placename')
    
class EventdateAdmin(admin.ModelAdmin):
    list_display = ('evtimestart',)

admin.site.register(Event, EventAdmin)
admin.site.register(Eventdate, EventdateAdmin)

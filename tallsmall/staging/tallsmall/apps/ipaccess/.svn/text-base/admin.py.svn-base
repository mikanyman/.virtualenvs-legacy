from django.contrib import admin
from django.utils.translation import ugettext_lazy as _ 
from tallsmall.apps.ipaccess.models import IPAccess

class IPAccessAdmin(admin.ModelAdmin):
    list_display = ('ip', 'user')

admin.site.register(IPAccess, IPAccessAdmin)
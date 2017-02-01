from django.contrib import admin
from synapse.segments.models import Segment
from django import forms

class SegmentAdmin(admin.ModelAdmin):

    exclude = ('author',)
    list_display = ('start', 'end', 'nomentype', 'nomen')
    
    
    
    # how do I set a foreign key to User to automatically be filled in with request.user?
    # people can only see/edit things they "own" (i.e., that they created) in the admin. 
    # http://docs.djangoproject.com/en/dev/ref/contrib/admin/
    # http://www.b-list.org/weblog/2008/dec/24/admin/
    
    def has_change_permission(self, request, obj=None):
        has_class_permission = super(SegmentAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.author.id:
            return False
        return True
    
    def queryset(self, request):
        return Segment.objects.filter(author=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()
    
    
        
    # Can "list_display" in a Django ModelAdmin display attributes of ForeignKey fields?
    # http://stackoverflow.com/questions/163823/can-list-display-in-a-django-modeladmin-display-attributes-of-foreignkey-fields
    # Auto-populating created_by field with Django admin site
    # http://code.djangoproject.com/wiki/CookBookNewformsAdminAndUser
    
    def fname_lname(self, obj):
        return "%s %s" % (obj.author.first_name, obj.author.last_name)
    fname_lname.short_description = 'Author'
    
admin.site.register(Segment, SegmentAdmin)
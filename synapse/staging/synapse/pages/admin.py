from django.contrib import admin
from synapse.pages.models import Page, Lang, Entry
from django import forms

### Custom Widgets: Forcier - Bissex - Chun, Python Web Development with Django, p. 152 f. (Widgets)

### Custom Widget
class MceContentWidget(forms.Textarea):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {}).update({
            'rows': 10,
            'cols': 80,
            'class': 'mce_content' # customized for TinyMCE textareas.js
            })
        super(MceContentWidget, self).__init__(*args, **kwargs)

### Custom Widget
class MceSummaryWidget(forms.Textarea):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {}).update({
            'rows': 4,
            'cols': 100,
            })
        super(MceSummaryWidget, self).__init__(*args, **kwargs)

class EntryAdmin(admin.ModelAdmin):

    exclude = ('author',)
    list_display = ('title', 'slug', 'created', 'fname_lname')
    #fieldsets = [
    #    (None, {'fields': ['title', 'slug', 'summary', 'content', 'page', 'author', 'lang']}),
    #]
    #prepopulated_fields = { 'slug': ['title'] }


    
    # Overriding a single field in the Django admin
    # http://www.kryogenix.org/days/2008/03/28/overriding-a-single-field-in-the-django-admin-using-newforms-admin
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'summary':
            kwargs['widget'] = MceSummaryWidget # custom widget
        if db_field.name == 'content':
            kwargs['widget'] = MceContentWidget
        #if db_field.name == 'sites':
        #    kwargs['widget'] = forms.CheckboxSelectMultiple
        return super(EntryAdmin,self).formfield_for_dbfield(db_field,**kwargs)


    
    # how do I set a foreign key to User to automatically be filled in with request.user?
    # people can only see/edit things they "own" (i.e., that they created) in the admin. 
    # http://docs.djangoproject.com/en/dev/ref/contrib/admin/
    # http://www.b-list.org/weblog/2008/dec/24/admin/
    
    def has_change_permission(self, request, obj=None):
        has_class_permission = super(EntryAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.author.id:
            return False
        return True
    
    def queryset(self, request):
        return Entry.objects.filter(author=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()



    # django-autoslug 1.3.8
    # http://pypi.python.org/pypi/django-autoslug/1.3.8
    
    

    
    # Can "list_display" in a Django ModelAdmin display attributes of ForeignKey fields?
    # http://stackoverflow.com/questions/163823/can-list-display-in-a-django-modeladmin-display-attributes-of-foreignkey-fields

    # Auto-populating created_by field with Django admin site
    # http://code.djangoproject.com/wiki/CookBookNewformsAdminAndUser

    def fname_lname(self, obj):
        return "%s %s" % (obj.author.first_name, obj.author.last_name)
    fname_lname.short_description = 'Author'



    class Media:
        js = ('/js/tiny_mce/tiny_mce.js', '/site_media/js/textareas.js') #  # C:/Python25/Lib/site-packages/django_tinymce-1.5.1.dev100-py2.5.egg/tinymce/media/tiny_mce
        css = {'screen': ('/site_media/css/admin.css',)}

    
admin.site.register(Page)
admin.site.register(Lang)
admin.site.register(Entry, EntryAdmin)


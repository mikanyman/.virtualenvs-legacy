# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _ 
from specs.portal.models import Application, Callable, Layout, Form, \
    FormLayout, Template, Menu, Menuitem, Tab, Page, Box, Celllocation, \
    Cell, Include, Entry, Entrystatus, Category, Feed

# ========== BEGINNING ==========
# http://www.djangosnippets.org/snippets/937/
from django import forms

class ReadOnlyWidget(forms.Widget):
    def __init__(self, original_value, display_value):
        self.original_value = original_value
        self.display_value = display_value

        super(ReadOnlyWidget, self).__init__()

    def render(self, name, value, attrs=None):
        if self.display_value is not None:
            return unicode(self.display_value)
        return unicode(self.original_value)

    def value_from_datadict(self, data, files, name):
        return self.original_value

class ReadOnlyAdminFields(object):
    def get_form(self, request, obj=None):
        form = super(ReadOnlyAdminFields, self).get_form(request, obj)

        if hasattr(self, 'readonly'):
            for field_name in self.readonly:
                if field_name in form.base_fields:

                    if hasattr(obj, 'get_%s_display' % field_name):
                        display_value = getattr(obj, 'get_%s_display' % field_name)()
                    else:
                        display_value = None

                    form.base_fields[field_name].widget = ReadOnlyWidget(getattr(obj, field_name, ''), display_value)
                    form.base_fields[field_name].required = False

        return form

# MALLI:
#class MyModelAdmin(ReadOnlyAdminFields, admin.ModelAdmin):
#    readonly = ('field1', 'field2',)
# ========== END ==========
    
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('label', 'order')

class CallableAdmin(admin.ModelAdmin):
    list_display = ('label', 'call', 'template')
    
class LayoutAdmin(admin.ModelAdmin):
    list_display = ('label', 'order')

class FormAdmin(admin.ModelAdmin):
    list_display = ('label', 'order')

class FormLayoutAdmin(admin.ModelAdmin):
    list_display = ('label', 'order')

class TemplateAdmin(admin.ModelAdmin):
    list_display = ('label', 'order')

class MenuAdmin(admin.ModelAdmin):
    list_display = ('label', 'order')
    
class MenuitemAdmin(admin.ModelAdmin):
    list_display = ('label', 'query_string', 'page', 'menu', 'order')
    
class TabAdmin(admin.ModelAdmin):
    list_display = ('label', 'order')
    
class PageAdmin(admin.ModelAdmin):
    list_display = ('visible_name', 'label', 'parent', 'application', 'order')

class BoxAdmin(admin.ModelAdmin):
    list_display = ('label', 'order')
    
class CelllocationAdmin(admin.ModelAdmin):
    list_display = ('label',)

class CellAdmin(admin.ModelAdmin):
    list_display = ('label', 'application', 'page', 'celllocation', 'box', 'order')
    
class IncludeAdmin(admin.ModelAdmin):
    list_display = ('label', 'path', 'order')
        
class EntryAdmin(admin.ModelAdmin):
    #readonly = ('created', 'modified')   
    list_display = ('label', 'creator', 'entrystatus', 'modified', 'profile')
    filter_horizontal = ('categories',) 

    # http://groups.google.fi/group/django-users/browse_thread/thread/12161ac3e8f8c96e/870e4c02c68b84b8?hl=fi&lnk=gst&q=format+datetime+field#870e4c02c68b84b8
    #def formfield_for_dbfield(self, db_field, **kwargs):
    #    field = super(EntryAdmin, self).formfield_for_dbfield(db_field, **kwargs) # Get the default field
    #    if db_field.name == "created": # Check if it's the one you want
    #        field.widget.attrs['class'] = "DateTimeInput" # Poke in the new 
    #    return field

    class Media:
        js = ('/media/wrk/specs/js/tiny_mce/tiny_mce.js', '/media/wrk/specs/js/tiny_mce/textareas.js')
        #js = ('/media/wrk/specs/js/tiny_mce/tiny_mce.js', '/media/wrk/specs/js/tiny_mce/TinyMCEAdmin.js')

    #fields = (
    #    ('Muokkaa', {'fields': ('slug', 'title', 'body', 'order')}),
    #)
    ##js = ('/media/wrk/specs/js/tiny_mce/tiny_mce.js','/media/wrk/specs/js/tiny_mce/textareas.js')
    #js = ['wrk/specs/js/tiny_mce/tiny_mce.js', 'wrk/specs/js/tiny_mce/textareas.js']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('visible_name', 'label',)
    filter_horizontal = ('pages',) 
    
class EntrystatusAdmin(admin.ModelAdmin):
    list_display = ('status', 'order', 'default_status')
        
class FeedAdmin(admin.ModelAdmin):
    list_display = ('label',)
    filter_horizontal = ('cells',)

admin.site.register(Application, ApplicationAdmin)
admin.site.register(Callable, CallableAdmin)
admin.site.register(Layout, LayoutAdmin)
admin.site.register(Form, FormAdmin)
admin.site.register(FormLayout, FormLayoutAdmin)
admin.site.register(Template, TemplateAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Menuitem, MenuitemAdmin)
admin.site.register(Tab, TabAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Box, BoxAdmin)
admin.site.register(Celllocation, CelllocationAdmin)
admin.site.register(Cell, CellAdmin)
admin.site.register(Include, IncludeAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Entrystatus, EntrystatusAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Feed, FeedAdmin)

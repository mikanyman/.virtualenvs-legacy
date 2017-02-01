## transdeco/galleria/admin.py

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _ 
from transdeco.galleria.models import Site, Artist, Photographer, Work, Image, TechniqueType


class SiteAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
#class WorkInline(admin.TabularInline):
#    model = Work
#    extra = 1
    
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('person_name', 'new_work')
    fieldsets = [
        (None, {'fields': ['person_name', 'label', 'birth_date', 'descriptive_note', 'new_work']}),
        (u'Taiteilijaan liittyvat kuvat', {'fields': ['artist_image_filename', 'square_image_filename_out', 'square_image_filename_in']}),
    ]
    #inlines = [WorkInline]
    
class PhotographerAdmin(admin.ModelAdmin):
    list_display = ('person_name',)
    

#class ImageInline(admin.StackedInline):
#    model = Image
#    extra = 0

class WorkAdmin(admin.ModelAdmin):
    list_display = ('title_text', 'artist', 'item_number', 'mater_tech_descr', 'creation_date', 'edition_size', 'dimensions_description', 'price', 'order', 'new_work')
    list_filter = ['artist']
    
    #inlines = [ImageInline]
    
class ImageAdmin(admin.ModelAdmin):
    list_display = ('work',)
    fieldsets = [
        (None,                 {'fields': ['original_image_filename', 'small_image_filename', 'medium_image_filename']}),
        (u'Kuvan metatiedot', {'fields': ['work', 'artist', 'photographer']}),
    ]
    list_filter = ['artist']
    
class TechniqueTypeAdmin(admin.ModelAdmin):
    list_display = ('label',)


admin.site.register(Site, SiteAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Photographer, PhotographerAdmin)
admin.site.register(Work, WorkAdmin) # Two ways to edit: here and in addition as inline under Artist
admin.site.register(Image, ImageAdmin)
admin.site.register(TechniqueType, TechniqueTypeAdmin)
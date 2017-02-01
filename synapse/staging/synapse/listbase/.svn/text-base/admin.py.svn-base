from django.contrib import admin
from synapse.listbase.models import Type, Member

class MemberInline(admin.TabularInline):
    
    model = Member
    extra = 1

class TypeAdmin(admin.ModelAdmin):
    
    list_display = ('label',)
    inlines = [MemberInline]

admin.site.register(Type, TypeAdmin)
admin.site.register(Member)


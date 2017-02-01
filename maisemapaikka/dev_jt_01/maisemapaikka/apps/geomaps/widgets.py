from django import forms
from django.db import models
from django.conf import settings

class LocationPickerWidget(forms.TextInput):
    class Media:
        css = {
            'all': (
                settings.ADMIN_MEDIA_PREFIX + 'css/location_picker.css',
            )
        }
    
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js',
            'http://www.google.com/jsapi?key=ABQIAAAA4NIx2jg3c_um-4n9lSUsUBQpzvvHaH8wLU269kY3vQUW6nVQBRTnCoPQWn83MqmlDy6i0XFj9TqLxw',
            settings.ADMIN_MEDIA_PREFIX + 'js/jquery.location_picker.js',
        )
        
    def __init__(self, attrs=None):
        super(LocationPickerWidget, self).__init__(attrs=attrs)

    def render(self, name, value, attrs=None):
        if attrs == None:
            attrs = {}
        attrs['class'] = 'location_picker'
        return super(LocationPickerWidget, self).render(name, value, attrs)
        
class LocationField(models.CharField):
    def formfield(self, **kwargs):
        kwargs['widget'] = LocationPickerWidget
        return super(LocationField, self).formfield(**kwargs)
from django import template
#from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='unescape_html')
#@stringfilter
def unescape_html(entry):
    entry = entry.replace("www", "CCCP")
    #entry = entry.replace("&quot;", "\"")
    #entry = entry.replace("&lt;", "<")
    #entry = entry.replace("&gt;", ">")
    # this has to be last:
    #entry = entry.replace("&amp;", "&")

    return entry



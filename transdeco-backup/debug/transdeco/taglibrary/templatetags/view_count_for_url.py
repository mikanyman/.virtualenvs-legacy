from django import template
from transdeco.counter.models import ViewCount

register = template.Library()

class ViewCountForURLNode(template.Node):
    def __init__(self, url, context_var):
        self.url = url
        self.context_var = context_var

    def render(self, context):

        url = template.resolve_variable(self.url, context)

        views_count = ViewCount.objects.filter(url=url)
        if not views_count:
            new_view_count = ViewCount(url=url).save()

        context[self.context_var] = ViewCount.objects.filter(url=url)[0].count

        return ''

@register.tag(name="view_count_for_url")
def do_viewcount_for_url(parser, token):
    """
    Example usage::

        {% view_count_for_url "/blog/" as count %}

    """
    bits = token.contents.split()
    if len(bits) != 4:
        raise template.TemplateSyntaxError("'%s' tag takes exactly three arguments" % bits[0])
    if bits[2] != 'as':
        raise template.TemplateSyntaxError("second argument to '%s' tag must be 'as'" % bits[0])
    return ViewCountForURLNode(bits[1], bits[3])


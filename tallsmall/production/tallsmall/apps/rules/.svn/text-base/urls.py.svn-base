from django.conf.urls.defaults import patterns, include, url
from django.views.generic import list_detail, create_update
from tallsmall.apps.rules.models import Rule, RuleForm

# list, detail
rule_info = {
    'queryset': Rule.objects.all(),
    'template_name': 'rules/display_rule.html',
}

# create, update
rule_form = {
  'form_class': RuleForm,
  'template_name': 'rules/add.html',
}

# delete
rule_delete = {
  'model': Rule,
  'post_delete_redirect': '/rules/list/',
  'template_name': 'rules/delete_confirm_rule.html',
}

# Modified
urlpatterns = patterns('',
    url(r'list/$', list_detail.object_list, rule_info, name='rule-list'), # LAST if $!
    url(r'create/$', create_update.create_object, rule_form, name='rule-create'),
    url(r'detail/(?P<object_id>\d+)/$', list_detail.object_detail, rule_info, name='rule-detail'),
    url(r'update/(?P<object_id>\d+)/$', create_update.update_object, rule_form, name='rule-update'),
    url(r'delete/(?P<object_id>\d+)/$', create_update.delete_object, rule_delete, name='rule-delete'),
)

# Original
#urlpatterns = patterns('',
#    url(r'(?P<object_id>\d+)/$', list_detail.object_detail, rule_info, name='rule-display'),
#    url(r'add/$', create_update.create_object, rule_form, name='rule-add'),
#    url(r'(?P<object_id>\d+)/modify/$', create_update.update_object, rule_form, name='rule-modify'),
#    url(r'(?P<object_id>\d+)/delete/$', create_update.delete_object, rule_delete, name='rule-delete'),
#    url(r'$', list_detail.object_list, rule_info, name='rule-displaytop'), # LAST!
#)

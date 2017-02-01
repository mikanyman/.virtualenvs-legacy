from django.views.generic.list_detail import object_list
from django.views.generic.list_detail import object_detail
from django.views.generic.create_update import update_object
from django.views.generic.create_update import delete_object
from specs.koputuksia.models import Juttu 
from specs.koputuksia.models import Category
from specs.koputuksia.models import Issue
from django.http import HttpResponseRedirect, HttpResponse

### IF-rakenne redundantti kun näytetään vain julkisut joissa on juttuja

def common_declarations(**params):
    global issue_num
    global num_of_articles_in_issue
    global context

    if params['issue_num_arg']:
        issue_num = params['issue_num_arg'] # nouda kyselysta
    else:
        issue_input = Issue.objects.filter(current__exact=True) # nouda tietokannasta
        issue_num = str(issue_input[0]) # esim. '1-2006'

    ## Yritys ratkaista virheilmoitus
    #issue_num = issue_num.encode('ascii')

    category_list = Category.objects.order_by('ordinal')
    dict_of_cats_nums = {}
    dict_of_ords_cats_nums = {}

    ### Looppaa lapi osastoluettelon
    ### Luo dictionaryn "dict_of_cats_nums", jossa pareina ovat kategorian nimi ja juttujen maara osastossa
    ### "dict_of_ords_cats_nums" sisakkainen dictionary ordinaali, kategorian nimi, juttua per kategoria

    for k in category_list:
        #num_of_cats_in_cur_cat = Juttu.objects.filter(categorys__name__exact=k.name, issue=params['issue_num_arg']).count()
        num_of_cats_in_cur_cat = Juttu.objects.filter(categorys__name__exact=k.name, issue=issue_num).count()
        dict_of_cats_nums[str(k.name)] = num_of_cats_in_cur_cat
        dict_of_ords_cats_nums[str(k.ordinal)] = {k.name: num_of_cats_in_cur_cat} # nested dict

    issue_list = Issue.objects.order_by('ordinal')
    dict_of_issues_nums = {}
    for k in issue_list:
        num_of_articles_in_cur_issue = Juttu.objects.filter(issue=k.name).count()
        dict_of_issues_nums[str(k.name)] = num_of_articles_in_cur_issue

    articles_in_issue = Juttu.objects.filter(issue=issue_num) # O-M filtteri
    num_of_articles_in_issue = len(articles_in_issue)

    # ========
    # context:
    # ========
    # issue_num               # Julkaisun numero, esim. 1-2006
    # dict_of_issues_nums     # dict julkaisun numero: juttujen lukumaara julkaisussa
    # dict_of_cats_nums       # dict osaston nimi: juttujen lukumaara osastossa
    # dict_of_ords_cats_nums  # dict jarjestysluku, (osasto, juttujen lukumaara osastossa)

    context = {
        'issue_num': issue_num,
        'dict_of_issues_nums': dict_of_issues_nums,
        'dict_of_cats_nums': dict_of_cats_nums,
        'dict_of_ords_cats_nums': dict_of_ords_cats_nums,
    }
    if params['cat_name_arg']:
        context['category_name'] = params['cat_name_arg']

def edit_view(request, issue_num, object_id):
    common_declarations(issue_num_arg=issue_num, cat_name_arg='')
    redirect_dir = '/sites/specs/koputuksia/'+issue_num+'/'+object_id+'/'
    return update_object(request, model=Juttu, object_id=object_id, post_save_redirect=redirect_dir, extra_context=context)

def del_view(request, issue_num, object_id):
    common_declarations(issue_num_arg=issue_num, cat_name_arg='')
    redirect_dir = '/sites/specs/koputuksia/'+issue_num+'/'
    return delete_object(request, model=Juttu, object_id=object_id, post_delete_redirect=redirect_dir, extra_context=context)

def id_view(request, issue_num, object_id):
    common_declarations(issue_num_arg=issue_num, cat_name_arg='')
    queryset = Juttu.objects.all()
    return object_detail(request, queryset, object_id, extra_context=context)

def root_view(request):
    common_declarations(issue_num_arg='', cat_name_arg='')
    queryset = Juttu.objects.filter(issue='1-2006')

    if num_of_articles_in_issue > 0:
        return object_list(request, queryset, extra_context=context)
    else:
        return HttpResponseRedirect('/sites/specs/errors/no_art_in_issue/') # flatfile

def issue_view(request, issue_num):
    common_declarations(issue_num_arg=issue_num, cat_name_arg='')
    queryset = Juttu.objects.filter(issue=issue_num) # filtteri
    if num_of_articles_in_issue > 0:
        return object_list(request, queryset, extra_context=context)
    else:
        return HttpResponseRedirect('/sites/specs/errors/no_art_in_issue/') # flatfile

def issue_category_view(request, issue_num, category_name):
    common_declarations(issue_num_arg=issue_num, cat_name_arg=category_name)
    queryset = Juttu.objects.filter(issue=issue_num, categorys__name=category_name) # M-M filtteri
    if num_of_articles_in_issue > 0:
        return object_list(request, queryset, extra_context = context)
    else:
        return HttpResponseRedirect('/sites/specs/errors/no_art_in_issue/') # flatfile

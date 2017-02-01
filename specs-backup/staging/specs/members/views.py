# -*- coding: UTF-8 -*-
# specs/members/views.py

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, HttpResponse
from django import forms
from django.db.models import Q
#from django.db import connection
from django.template import RequestContext
#from django.newforms import form_for_model, form_for_instance

from specs.modules import PortalContext
from specs.members.models import Member, Applicant
from specs.members.forms import \
    TunnistetiedotForm, JasentiedotForm, YhteystiedotForm, \
    HenkKokotiedotForm, VaatKokotiedotForm, YritystiedotForm, \
    DataForm, MuutForm, JasenhakemusForm
    
""" Generic views """
from django.views.generic.create_update import create_object
    
def application_create(request, **kwargs):
    return create_object(request, 
        form_class=JasenhakemusForm, 
        template_name='members/jasenhakemus_form.html'
        )

def application_update(request, **kwargs):
    return update_object(request, 
        form_class=JasenhakemusForm, 
        object_id=kwargs['object_id'], 
        template_name='members/jasenhakemus_form.html'
        )

"""
def application(request, url_lang, url_profile, url_event, url_app, url_pg):
    
    form_completed = '0'
    applicant_id = ''
    
    if request.method == 'POST':
        applicant_form = JasenhakemusForm(request.POST)
        
        if applicant_form.is_valid():
            
            applicant = Applicant()
            
            applicant.etunimi = jasenhakemus_form.cleaned_data['etunimi']
            applicant.sukunimi = jasenhakemus_form.cleaned_data['sukunimi']
            applicant.katuosoite = jasenhakemus_form.cleaned_data['katuosoite']
            applicant.postinumero = jasenhakemus_form.cleaned_data['postinumero']
            applicant.postitoimipaikka = jasenhakemus_form.cleaned_data['postitoimipaikka']
            applicant.puhelin = jasenhakemus_form.cleaned_data['puhelin']
            applicant.email = jasenhakemus_form.cleaned_data['email']
            applicant.save()
            form_completed = '1'
            applicant_id = applicant.id 
            #next = '/'+url_lang+'/'+url_profile+'/'+url_event+'/'+url_app+'/'+url_pg+'/'
            #return HttpResponseRedirect(next)
        else:
            form_completed = '0'
    else:
        applicant_form = JasenhakemusForm()
            
    context = {
        'applicant_form': applicant_form,
        'form_completed': form_completed,
        'applicant_id': applicant_id
        }
    return render_to_response('members/application.html', context, context_instance=RequestContext(request))
"""

def members_list(request, url_lang, url_profile, url_event, url_app, url_pg):
    
    cls = request.GET.get('class', '')
    
    if cls == 'reg': filter = "filter(Q(varsinainen=True) & Q(tila='act')).order_by('sukunimi', 'etunimi', 'jasennumero')"
    elif cls == 'corp': filter = "filter(Q(yri=True) & Q(tila='act'))"
    elif cls == 'hon': filter = "filter(Q(kunnia=True) & Q(tila='act')).order_by('sukunimi', 'etunimi', 'jasennumero')"
    elif cls == 'all': filter = "filter(Q(tila='act') & Q(yri=False)).order_by('sukunimi', 'etunimi', 'jasennumero')"
    elif cls == 'mail': filter = "filter(Q(tila='act') & (Q(varsinainen=True) | Q(kunnia=True) | Q(yri=True) | Q(kannatus=True))).order_by('sukunimi', 'etunimi', 'jasennumero')"
    elif cls == 'send': filter = "filter(Q(tila='act') & (Q(varsinainen=True) | Q(kunnia=True) | Q(yri=True) | Q(kannatus=True))).order_by('sukunimi', 'etunimi', 'jasennumero')"
    elif cls == 'new': filter = "filter(\
            ((Q(varsinainen=False) & Q(perhe=False) & Q(kannatus=False) & Q(kunnia=False) & Q(yri=False)) & ((Q(tila='act') | Q(tila='pass')))) | \
            ((Q(tila='act') | Q(tila='pass')) & Q(uudet_jasenet=True))\
        ).order_by('sukunimi', 'etunimi', 'jasennumero')"
    elif cls == 'trash': filter = "filter(tila='trash').order_by('sukunimi')"
    elif cls == 'query':
        mid = request.GET.get('mid', '')
        if mid:
            filter = "filter(jasennumero=%s).order_by('sukunimi', 'etunimi', 'jasennumero')" % mid
    else: filter = "filter(varsinainen=True).order_by('sukunimi', 'etunimi', 'jasennumero')" # TO-DO: Ohjaa virhesivulle tai oletussivulle
    
    context = PortalContext.context(request, url_lang, url_profile, url_event, url_app, url_pg,\
        call='list', model='Member', filter=filter, template_name_part='members', cls=cls)
        
    # TO-DO: hae template layout -asetuksista
    template = 'cellsets/2col_sidebar_right.html'
    
    #l_paym = {}
    #l_paym = {'aaa': '888888'}
    #context.update(l_paym)
    
    response = render_to_response(template, context, context_instance=RequestContext(request))
    return response

def members_pass(request, url_lang, url_profile, url_event, url_app, url_pg):

    kdict = {}
    for k, v in request.POST.iteritems():
        if request.POST[k]:
            exec "kdict['%s'] = %s" % (k, v)
    
    import psycopg2
    connection = psycopg2.connect("dbname='specs' user='specs' password='specs'")
    cursor = connection.cursor()
    for k, v in kdict.iteritems():
        cursor.execute("""
            UPDATE members_member
            SET tila='%s'
            WHERE id=%s""" % (v[0], k))
    connection.commit()    
    connection.close()
    
    next = '/'+url_lang+'/'+url_profile+'/'+url_event+'/'+url_app+'/members_list/?cls=mail'
    return HttpResponseRedirect(next)

def members_latest_id(request, url_lang, url_profile, url_event, url_app, url_pg):
    
    member = Member.objects.latest('object_created')
    exec "next = '/%s/%s/%s/%s/%s/%s/?call=update'" % (url_lang, url_profile, url_event, url_app, url_pg, member.id)
    return HttpResponseRedirect(next)

def member_events(request, url_lang, url_profile, url_event, url_app, url_pg, object_id):
    return HttpResponse('EVENT...')

def members_detail(request, url_lang, url_profile, url_event, url_app, url_pg, object_id=None):
    
    call = request.GET.get('call', '')
    if call == 'update':
        next = '/'+url_lang+'/'+url_profile+'/'+url_event+'/'+url_app+'/'+url_pg+'/'+object_id+'/?call='+call
    elif call == 'create':
        next = '/'+url_lang+'/'+url_profile+'/'+url_event+'/'+url_app+'/'+url_pg+'/latest_id/?call=update'
    elif call == 'delete':
        next = '/'+url_lang+'/'+url_profile+'/'+url_event+'/'+url_app+'/members_list/?call=all'
            
    ### POST
    if request.POST:
                
        ### Vastaanotto
        tunnistetiedot_form_dict = {
            'arvo': request.POST.get('arvo', ''),
            'etunimi': request.POST.get('etunimi', ''),
            'sukunimi': request.POST.get('sukunimi', ''),
            'ent_sukunimi': request.POST.get('ent_sukunimi', '')
            }
        jasentiedot_form_dict = {
            'jasennumero': request.POST.get('jasennumero', ''),
            'liittymisvuosi': request.POST.get('liittymisvuosi', ''),
            'eroaminen': request.POST.get('eroaminen', ''),
            'varsinainen': request.POST.get('varsinainen', ''),
            'perhe': request.POST.get('perhe', ''),
            'kannatus': request.POST.get('kannatus', ''),
            'kunnia': request.POST.get('kunnia', ''),
            'yri': request.POST.get('yri', ''),
            'uudet_jasenet': request.POST.get('uudet_jasenet', ''),
            'tila': request.POST.get('tila', '')
            }
        yhteystiedot_form_dict = {
            'yritys': request.POST.get('yritys', ''),
            'postiosoite': request.POST.get('postiosoite', ''),
            'postitoimipaikka': request.POST.get('postitoimipaikka', ''),
            'postinumeroalue': request.POST.get('postinumeroalue', ''),
            'maa_osoitteessa': request.POST.get('maa_osoitteessa', ''),
            'laani': request.POST.get('laani', ''),
            'puhelin_gsm_faksi': request.POST.get('puhelin_gsm_faksi', ''),
            'email': request.POST.get('email', '')
            }
        henk_kokotiedot_form_dict = {
            'syntymavuosi': request.POST.get('syntymavuosi', ''),
            'mies': request.POST.get('mies', ''),
            'nainen': request.POST.get('nainen', ''),
            'pituustyyppi': request.POST.get('pituustyyppi', ''),
            'pituus': request.POST.get('pituus', ''),
            'vartalotyyppi': request.POST.get('vartalotyyppi', ''),
            'paanymparys': request.POST.get('paanymparys', '')
            }
        vaat_kokotiedot_form_dict = {
            'kenkakoko': request.POST.get('kenkakoko', ''),
            'vaatekoko': request.POST.get('vaatekoko', ''),
            'kasinekoko': request.POST.get('kasinekoko', '')
            }
        yritystiedot_form_dict = {
            'messuavustus': request.POST.get('messuavustus', ''),
            'muut_liikkeet': request.POST.get('muut_liikkeet', '')
            }
        data_form_dict = {
            'tietosuoja_1': request.POST.get('tietosuoja_1', ''),
            'tietosuoja_2': request.POST.get('tietosuoja_2', ''),
            'tietosuoja_3': request.POST.get('tietosuoja_3', ''),
            'tietosuoja_4': request.POST.get('tietosuoja_4', ''),
            'tietosuoja_5': request.POST.get('tietosuoja_5', ''),
            'tiedot_paivitetty': request.POST.get('tiedot_paivitetty', '')
            }
        muut_form_dict = {
            'muuta': request.POST.get('muuta', '')
            }

        ### Validointi ja tallennus
        member = Member()
        
        if call == 'update' or call == 'delete':
            member.id = object_id
            date_dict = Member.objects.select_dates(object_id)
            member.object_created = date_dict['object_created']
        
        tunnistetiedot_form = TunnistetiedotForm(tunnistetiedot_form_dict)
        if tunnistetiedot_form.is_valid():
            member.arvo = tunnistetiedot_form.cleaned_data['arvo']
            member.etunimi = tunnistetiedot_form.cleaned_data['etunimi']
            member.sukunimi = tunnistetiedot_form.cleaned_data['sukunimi']
            member.ent_sukunimi = tunnistetiedot_form.cleaned_data['ent_sukunimi']
        
        jasentiedot_form = JasentiedotForm(jasentiedot_form_dict)
        if jasentiedot_form.is_valid():
            member.jasennumero = jasentiedot_form.cleaned_data['jasennumero']
            member.liittymisvuosi = jasentiedot_form.cleaned_data['liittymisvuosi']
            member.eroaminen = jasentiedot_form.cleaned_data['eroaminen']
            member.varsinainen = jasentiedot_form.cleaned_data['varsinainen']
            member.perhe = jasentiedot_form.cleaned_data['perhe']
            member.kannatus = jasentiedot_form.cleaned_data['kannatus']
            member.kunnia = jasentiedot_form.cleaned_data['kunnia']
            member.yri = jasentiedot_form.cleaned_data['yri']
            member.uudet_jasenet = jasentiedot_form.cleaned_data['uudet_jasenet']
            if call == 'update':
                member.tila = jasentiedot_form.cleaned_data['tila']
            elif call == 'delete':
                member.tila = 'del'
        
        yhteystiedot_form = YhteystiedotForm(yhteystiedot_form_dict)
        if yhteystiedot_form.is_valid():
            member.yritys = yhteystiedot_form.cleaned_data['yritys']
            member.postiosoite = yhteystiedot_form.cleaned_data['postiosoite']
            member.postitoimipaikka = yhteystiedot_form.cleaned_data['postitoimipaikka']
            member.postinumeroalue = yhteystiedot_form.cleaned_data['postinumeroalue']
            member.maa_osoitteessa = yhteystiedot_form.cleaned_data['maa_osoitteessa']
            member.laani = yhteystiedot_form.cleaned_data['laani']
            member.puhelin_gsm_faksi = yhteystiedot_form.cleaned_data['puhelin_gsm_faksi']
            member.email = yhteystiedot_form.cleaned_data['email']
        
        henk_kokotiedot_form = HenkKokotiedotForm(henk_kokotiedot_form_dict)
        if henk_kokotiedot_form.is_valid():
            member.syntymavuosi = henk_kokotiedot_form.cleaned_data['syntymavuosi']
            member.mies = henk_kokotiedot_form.cleaned_data['mies']
            member.nainen = henk_kokotiedot_form.cleaned_data['nainen']
            member.pituustyyppi = henk_kokotiedot_form.cleaned_data['pituustyyppi']
            member.pituus = henk_kokotiedot_form.cleaned_data['pituus']
            member.vartalotyyppi = henk_kokotiedot_form.cleaned_data['vartalotyyppi']
            member.paanymparys = henk_kokotiedot_form.cleaned_data['paanymparys']
        
        vaat_kokotiedot_form = VaatKokotiedotForm(vaat_kokotiedot_form_dict)
        if vaat_kokotiedot_form.is_valid():
            member.kenkakoko = vaat_kokotiedot_form.cleaned_data['kenkakoko']
            member.vaatekoko = vaat_kokotiedot_form.cleaned_data['vaatekoko']
            member.kasinekoko = vaat_kokotiedot_form.cleaned_data['kasinekoko']
        
        yritystiedot_form = YritystiedotForm(yritystiedot_form_dict)
        if yritystiedot_form.is_valid():
            member.messuavustus = yritystiedot_form.cleaned_data['messuavustus']
            member.muut_liikkeet = yritystiedot_form.cleaned_data['muut_liikkeet']
        
        datatiedot_form = DataForm(data_form_dict)
        if datatiedot_form.is_valid():
            member.tietosuoja_1 = datatiedot_form.cleaned_data['tietosuoja_1']
            member.tietosuoja_2 = datatiedot_form.cleaned_data['tietosuoja_2']
            member.tietosuoja_3 = datatiedot_form.cleaned_data['tietosuoja_3']
            member.tietosuoja_4 = datatiedot_form.cleaned_data['tietosuoja_4']
            member.tietosuoja_5 = datatiedot_form.cleaned_data['tietosuoja_5']
            member.tiedot_paivitetty = datatiedot_form.cleaned_data['tiedot_paivitetty']
        
        muut_tiedot_form = MuutForm(muut_form_dict)
        if muut_tiedot_form.is_valid():
            member.muuta = muut_tiedot_form.cleaned_data['muuta']

        member.save()
        return HttpResponseRedirect(next)
    
    ### GET
    if call == 'update' or call == 'view' or call == 'delete':
        
        t = Member.objects.select_tunnistetiedot(object_id)
        tunnistetiedot_form = TunnistetiedotForm(t)
        j = Member.objects.select_jasentiedot(object_id)
        jasentiedot_form = JasentiedotForm(j)
        y = Member.objects.select_yhteystiedot(object_id)
        yhteystiedot_form = YhteystiedotForm(y)
        h = Member.objects.select_henkkokotiedot(object_id)
        henk_kokotiedot_form = HenkKokotiedotForm(h)
        v = Member.objects.select_vaatkokotiedot(object_id)
        vaat_kokotiedot_form = VaatKokotiedotForm(v)
        y = Member.objects.select_yritystiedot(object_id)
        yritystiedot_form = YritystiedotForm(y)
        d = Member.objects.select_datatiedot(object_id)
        datatiedot_form = DataForm(d)
        m = Member.objects.select_muuttiedot(object_id)
        muut_tiedot_form = MuutForm(m)
                
        exec "filter = 'get(id=%s)'" % object_id
    
    elif call == 'create' or call == 'search':
        
        tunnistetiedot_form = TunnistetiedotForm()
        jasentiedot_form = JasentiedotForm()
        yhteystiedot_form = YhteystiedotForm()
        henk_kokotiedot_form = HenkKokotiedotForm()
        vaat_kokotiedot_form = VaatKokotiedotForm()
        yritystiedot_form = YritystiedotForm()
        datatiedot_form = DataForm()
        muut_tiedot_form = MuutForm()
            
    #clvuds_dict = {'call': call, 'model': 'Member', 'filter': filter, 'template': 'members'} POISTA
    context = PortalContext.context(request, url_lang, url_profile, url_event, url_app, url_pg,\
        call=call, model='Member', filter=filter, template_name_part='members',\
        tunnistetiedot_form = tunnistetiedot_form,
        jasentiedot_form = jasentiedot_form,
        yhteystiedot_form = yhteystiedot_form,
        henk_kokotiedot_form = henk_kokotiedot_form,
        vaat_kokotiedot_form = vaat_kokotiedot_form,
        yritystiedot_form = yritystiedot_form,
        datatiedot_form = datatiedot_form,
        muut_tiedot_form = muut_tiedot_form
        )
    
    # TO-DO: hae template layout -asetuksista
    template = 'cellsets/2col_sidebar_right.html'
    response = render_to_response(template, context, context_instance=RequestContext(request))
    return response

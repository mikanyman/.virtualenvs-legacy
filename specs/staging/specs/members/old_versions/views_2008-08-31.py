# -*- coding: UTF-8 -*-
# specs/members/views.py

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from specs.modules import PortalContext
from django.newforms import form_for_model, form_for_instance
from specs.members.models import Member

from specs.members.forms import TunnistetiedotForm, JasentiedotForm, YhteystiedotForm, \
                                HenkKokotiedotForm, VaatKokotiedotForm, YritystiedotForm, \
                                DataForm, MuutForm

def members_list(request, url_status, url_project, url_lang, url_profile, url_event, url_app, url_pg):
        
    if url_pg == 'members_person':
        filter = 'filter(varsinainen=True)'
    elif url_pg == 'members_corp':
        filter = 'filter(yri=True)'
    elif url_pg == 'members_hon':
        filter = 'filter(kunnia=True)'
    elif url_pg == 'members_all':
        filter = 'all()'
    elif url_pg == 'members_mail':
        filter = 'all()'
    else:
        pass # TO-DO: Ohjaa virhesivulle tai oletussivulle
    
    clvuds_dict = {'call': 'list', 'model': 'Member', 'filter': filter, 'template': 'members'}
    context = PortalContext.context(request, url_status, url_project, url_lang, url_profile, url_event, url_app, url_pg, clvuds_dict)
    
    # TO-DO: hae template layout -asetuksista
    template = 'cellsets/2col_sidebar_right.html'
    response = render_to_response(template, context, context_instance=RequestContext(request))
    return response

def members_detail(request, url_status, url_project, url_lang, url_profile, url_event, url_app, url_pg, object_id):
    
    call = request.GET.get('call', '')
    next = '/'+url_status+'/'+url_project+'/'+url_lang+'/'+url_profile+'/'+url_event+'/'+url_app+'/'+url_pg+'/'+object_id+'/?call='+call
        
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
        
        if call == 'update':
            member.id = object_id
        
        tunnistetiedot_form = TunnistetiedotForm(tunnistetiedot_form_dict)
        if tunnistetiedot_form.is_valid():
            member.arvo = tunnistetiedot_form.clean_data['arvo']
            member.etunimi = tunnistetiedot_form.clean_data['etunimi']
            member.sukunimi = tunnistetiedot_form.clean_data['sukunimi']
            member.ent_sukunimi = tunnistetiedot_form.clean_data['ent_sukunimi']
            
        jasentiedot_form = JasentiedotForm(jasentiedot_form_dict)
        if jasentiedot_form.is_valid():
             member.liittymisvuosi = jasentiedot_form.clean_data['liittymisvuosi']
             member.eroaminen = jasentiedot_form.clean_data['eroaminen']
             member.varsinainen = jasentiedot_form.clean_data['varsinainen']
             member.perhe = jasentiedot_form.clean_data['perhe']
             member.kannatus = jasentiedot_form.clean_data['kannatus']
             member.kunnia = jasentiedot_form.clean_data['kunnia']
             member.uudet_jasenet = jasentiedot_form.clean_data['uudet_jasenet']
             member.tila = jasentiedot_form.clean_data['tila']
            
        yhteystiedot_form = YhteystiedotForm(yhteystiedot_form_dict)
        if yhteystiedot_form.is_valid():
            member.yritys = yhteystiedot_form.clean_data['yritys']
            member.postiosoite = yhteystiedot_form.clean_data['postiosoite']
            member.postitoimipaikka = yhteystiedot_form.clean_data['postitoimipaikka']
            member.postinumeroalue = yhteystiedot_form.clean_data['postinumeroalue']
            member.maa_osoitteessa = yhteystiedot_form.clean_data['maa_osoitteessa']
            member.laani = yhteystiedot_form.clean_data['laani']
            member.puhelin_gsm_faksi = yhteystiedot_form.clean_data['puhelin_gsm_faksi']
            member.email = yhteystiedot_form.clean_data['email']
            
        henk_kokotiedot_form = HenkKokotiedotForm(henk_kokotiedot_form_dict)
        if henk_kokotiedot_form.is_valid():
            member.syntymavuosi = henk_kokotiedot_form.clean_data['syntymavuosi']
            member.mies = henk_kokotiedot_form.clean_data['mies']
            member.nainen = henk_kokotiedot_form.clean_data['nainen']
            member.pituustyyppi = henk_kokotiedot_form.clean_data['pituustyyppi']
            member.pituus = henk_kokotiedot_form.clean_data['pituus']
            member.vartalotyyppi = henk_kokotiedot_form.clean_data['vartalotyyppi']
            member.paanymparys = henk_kokotiedot_form.clean_data['paanymparys']
            
        vaat_kokotiedot_form = VaatKokotiedotForm(vaat_kokotiedot_form_dict)
        if vaat_kokotiedot_form.is_valid():
            member.kenkakoko = vaat_kokotiedot_form.clean_data['kenkakoko']
            member.vaatekoko = vaat_kokotiedot_form.clean_data['vaatekoko']
            member.kasinekoko = vaat_kokotiedot_form.clean_data['kasinekoko']
            
        yritystiedot_form = YritystiedotForm(yritystiedot_form_dict)
        if yritystiedot_form.is_valid():
            member.messuavustus = yritystiedot_form.clean_data['messuavustus']
            member.muut_liikkeet = yritystiedot_form.clean_data['muut_liikkeet']
            
        datatiedot_form = DataForm(data_form_dict)
        if datatiedot_form.is_valid():
            member.tietosuoja_1 = datatiedot_form.clean_data['tietosuoja_1']
            member.tietosuoja_2 = datatiedot_form.clean_data['tietosuoja_2']
            member.tietosuoja_3 = datatiedot_form.clean_data['tietosuoja_3']
            member.tietosuoja_4 = datatiedot_form.clean_data['tietosuoja_4']
            member.tietosuoja_5 = datatiedot_form.clean_data['tietosuoja_5']
            member.tiedot_paivitetty = datatiedot_form.clean_data['tiedot_paivitetty']
            
        muut_tiedot_form = MuutForm(muut_form_dict)
        if muut_tiedot_form.is_valid():
            member.muuta = muut_tiedot_form.clean_data['muuta']

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
                
    elif call == 'create' or call == 'search':
        
        tunnistetiedot_form = TunnistetiedotForm()
        jasentiedot_form = JasentiedotForm()
        yhteystiedot_form = YhteystiedotForm()
        henk_kokotiedot_form = HenkKokotiedotForm()
        vaat_kokotiedot_form = VaatKokotiedotForm()
        yritystiedot_form = YritystiedotForm()
        datatiedot_form = DataForm()
        muut_tiedot_form = MuutForm()
        
    exec "filter = 'get(id=%s)'" % object_id
    
    clvuds_dict = {'call': call, 'model': 'Member', 'filter': filter, 'template': 'members'}
    forms_dict = {
        'tunnistetiedot_form': tunnistetiedot_form,
        'jasentiedot_form': jasentiedot_form,
        'yhteystiedot_form': yhteystiedot_form,
        'henk_kokotiedot_form': henk_kokotiedot_form,
        'vaat_kokotiedot_form': vaat_kokotiedot_form,
        'yritystiedot_form': yritystiedot_form,
        'datatiedot_form': datatiedot_form,
        'muut_tiedot_form': muut_tiedot_form,
        }
    context = PortalContext.context(request, url_status, url_project, url_lang, url_profile, url_event, url_app, url_pg, clvuds_dict, forms_dict)
    
    # TO-DO: hae template layout -asetuksista
    template = 'cellsets/2col_sidebar_right.html'
    response = render_to_response(template, context, context_instance=RequestContext(request))
    return response

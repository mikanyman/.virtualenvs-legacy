# specs/choe/views.py

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.views.generic.list_detail import object_list
from django.views.generic.create_update import create_object
from specs.choe.models import Entry, EntryForm

def list_entries(request):

    ### GENERIC VIEWS
    queryset = Entry.objects.all()
    return object_list(request, queryset, paginate_by = 20)
    
def create_entry(request):
   
    if request.method == 'POST':
        form = EntryForm(request.POST)
        entry = Entry()

        if form.is_valid():
            
                             
            entry.ip_address = request.META['REMOTE_ADDR']
            first_created = form.cleaned_data['first_created']
            
            ### Mitattaaajan yhteystiedot
            entry.sukunimi = form.cleaned_data['sukunimi']
            entry.etunimi = form.cleaned_data['etunimi']
            entry.puhelinnumero = form.cleaned_data['puhelinnumero']
            entry.email = form.cleaned_data['email']

            ### Mitattavan yhteystiedot
            entry.sukunimi = form.cleaned_data['sukunimi']
            entry.etunimi = form.cleaned_data['etunimi']
            entry.katuosoite = form.cleaned_data['katuosoite']
            entry.postinumero = form.cleaned_data['postinumero']
            entry.postitoimipaikka = form.cleaned_data['postitoimipaikka']
            entry.puhelinnumero = form.cleaned_data['puhelinnumero']
            entry.email = form.cleaned_data['email']

            ### Henkilotiedot
            entry.sukupuoli = form.cleaned_data['sukupuoli']
            entry.ikaryhma = form.cleaned_data['ikaryhma']
            entry.kenkakoko = form.cleaned_data['kenkakoko']

            ### Mittatiedot
            entry.vartalon_pituus = form.cleaned_data['vartalon_pituus']
            entry.rinnan_ymparys = form.cleaned_data['rinnan_ymparys']
            entry.vyotaron_ymparys = form.cleaned_data['vyotaron_ymparys']
            entry.lantion_ymparys = form.cleaned_data['lantion_ymparys']
            entry.jalan_sivupituus = form.cleaned_data['jalan_sivupituus']
            entry.saaren_takapituus = form.cleaned_data['saaren_takapituus']
            entry.pohkeen_ymparys = form.cleaned_data['pohkeen_ymparys']
            entry.nilkan_ymparys = form.cleaned_data['nilkan_ymparys']
            entry.jalkapohjan_pituus = form.cleaned_data['jalkapohjan_pituus']
            entry.pakian_ymparys = form.cleaned_data['pakian_ymparys']
            entry.jalkama = form.cleaned_data['jalkama']

            ### Jalkojen terveyteen liittyvia ongelmia
            entry.jalkakipuja = form.cleaned_data['jalkakipuja']
            entry.missa_jalkakipuja = form.cleaned_data['missa_jalkakipuja']
            entry.kipuasteikko = form.cleaned_data['kipuasteikko']
            entry.asiantuntija = form.cleaned_data['asiantuntija']
            entry.tukipohjallinen_suositeltu = form.cleaned_data['tukipohjallinen_suositeltu']
            entry.tukipohjallinen_kaytossa = form.cleaned_data['tukipohjallinen_kaytossa']
            entry.asentovirhe = form.cleaned_data['asentovirhe']
            entry.kovettumia = form.cleaned_data['kovettumia']
            entry.vaivasenluu = form.cleaned_data['vaivasenluu']
            entry.pitk_laskeuma = form.cleaned_data['pitk_laskeuma']
            entry.poik_laskeuma = form.cleaned_data['poik_laskeuma']
            entry.vasaravarpaat = form.cleaned_data['vasaravarpaat']
            entry.muuta_vaivaa = form.cleaned_data['muuta_vaivaa']
            
            entry.save()
            return HttpResponseRedirect('/wrk/specs/choe/create/')
        
        else:
            context = {
                'entry_form': form,
            }
            return render_to_response('choe/entry_form.html', context)
        
    else:

        form = EntryForm()
        context = {
            'entry_form': form,
        }
    
        ### GENERIC VIEWS
        return create_object(request, Entry, extra_context = context)
        #post_save_redirect = "/specs/choe/?page=%(id)s/", 

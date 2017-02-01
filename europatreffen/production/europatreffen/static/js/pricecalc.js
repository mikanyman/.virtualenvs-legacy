// http://www.javascript-coder.com/files/calculation/cakeform.html

function prsu1welcomePrice() {
    var prsu1welcomePrice=0;
    var theForm = document.forms["etregform"];
    var id_prsu1welcome = theForm.elements["id_prsu1welcome"];
    if(id_prsu1welcome.checked==true)
    {prsu1welcomePrice=27;}
    return prsu1welcomePrice;
}
function prmonokiaPrice() {
    var prmonokiaPrice=0;
    var theForm = document.forms["etregform"];
    var id_prmonokia = theForm.elements["id_prmonokia"];
    if(id_prmonokia.checked==true)
    {prmonokiaPrice=27;}
    return prmonokiaPrice;
}
function prmotamperePrice() {
    var prmotamperePrice=0;
    var theForm = document.forms["etregform"];
    var id_prmotampere = theForm.elements["id_prmotampere"];
    if(id_prmotampere.checked==true)
    {prmotamperePrice=27;}
    return prmotamperePrice;
}
function prmo2welcomePrice() {
    var prmo2welcomePrice=0;
    var theForm = document.forms["etregform"];
    var id_prmo2welcome = theForm.elements["id_prmo2welcome"];
    if(id_prmo2welcome.checked==true)
    {prmo2welcomePrice=53;}
    return prmo2welcomePrice;
}
function prtulunchPrice() {
    var prtulunchPrice=0;
    var theForm = document.forms["etregform"];
    var id_prtulunch = theForm.elements["id_prtulunch"];
    if(id_prtulunch.checked==true)
    {prtulunchPrice=8;}
    return prtulunchPrice;
}
function prtuboatPrice() {
    var prtuboatPrice=0;
    var theForm = document.forms["etregform"];
    var id_prtuboat = theForm.elements["id_prtuboat"];
    if(id_prtuboat.checked==true)
    {prtuboatPrice=40;}
    return prtuboatPrice;
}
function prwehelsinkiPrice() {
    var prwehelsinkiPrice=0;
    var theForm = document.forms["etregform"];
    var id_prwehelsinki = theForm.elements["id_prwehelsinki"];
    if(id_prwehelsinki.checked==true)
    {prwehelsinkiPrice=68;}
    return prwehelsinkiPrice;
}
function prwesuomenlinnaPrice() {
    var prwesuomenlinnaPrice=0;
    var theForm = document.forms["etregform"];
    var id_prwesuomenlinna = theForm.elements["id_prwesuomenlinna"];
    if(id_prwesuomenlinna.checked==true)
    {prwesuomenlinnaPrice=17;}
    return prwesuomenlinnaPrice;
}
function prthujuhannusPrice() {
    var prthujuhannusPrice=0;
    var theForm = document.forms["etregform"];
    var id_prthujuhannus = theForm.elements["id_prthujuhannus"];
    if(id_prthujuhannus.checked==true)
    {prthujuhannusPrice=55;}
    return prthujuhannusPrice;
}
function prfrisaunapisPrice() {
    var prfrisaunapisPrice=0;
    var theForm = document.forms["etregform"];
    var id_prfrisaunapis = theForm.elements["id_prfrisaunapis"];
    if(id_prfrisaunapis.checked==true)
    {prfrisaunapisPrice=37;}
    return prfrisaunapisPrice;
}
function prsatgalaPrice() {
    var prsatgalaPrice=0;
    var theForm = document.forms["etregform"];
    var id_prsatgala = theForm.elements["id_prsatgala"];
    if(id_prsatgala.checked==true)
    {prsatgalaPrice=70;}
    return prsatgalaPrice;
}
function nontallclubPrice() {
    var nontallclubPrice=0;
    var theForm = document.forms["etregform"];
    var id_nontallclub = theForm.elements["id_nontallclub"];
    if(id_nontallclub.checked==true)
    {nontallclubPrice=20;}
    return nontallclubPrice;
}

function calculateTotal() {
    var eventsPrice = prsu1welcomePrice()+prmonokiaPrice()+prmotamperePrice()+prmo2welcomePrice()+prtulunchPrice()+prtuboatPrice()+prwehelsinkiPrice()+prwesuomenlinnaPrice()+prthujuhannusPrice()+prfrisaunapisPrice()+prsatgalaPrice()+8+nontallclubPrice();
    var divobj = document.getElementById('totalPrice');
    divobj.style.display='block';
    divobj.innerHTML = eventsPrice; // "Total Price For the Events $" +
    
    // put total price in hidden field:
    var hiddenobj = document.getElementById('total');
    hiddenobj.style.display='block';
    hiddenobj.value = eventsPrice;
}
//function hideTotal() {
//    var divobj = document.getElementById('totalPrice');
//    divobj.style.display='none';
//}
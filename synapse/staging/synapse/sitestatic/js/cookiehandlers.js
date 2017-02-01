/* Source: http://www.quirksmode.org/js/cookies.html */

function createCookie(name,value,days) {
	if (days) {
		var date = new Date();
		date.setTime(date.getTime()+(days*24*60*60*1000));
		var expires = "; expires="+date.toGMTString();
	}
	else var expires = "";
	document.cookie = name+"="+value+expires+"; path=/";
}

function readCookie(name) {
	var nameEQ = name + "=";
	var ca = document.cookie.split(';');
	for(var i=0;i < ca.length;i++) {
		var c = ca[i];
		while (c.charAt(0)==' ') c = c.substring(1,c.length);
		if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
	}
	return null;
}

function eraseCookie(name) {
	createCookie(name,"",-1);
}


/* Expected input: 'cur_page', '#pagename' */
function setcookie(cname, cval) {
    // eraseCookie('cname')       // eraseCookie(name)
    createCookie(cname, cval, 1)  // createCookie(name,value,days)
    }
function returnCookie(cname) {
    var cval = readCookie(cname); // readCookie(name)
    return cval;
    }



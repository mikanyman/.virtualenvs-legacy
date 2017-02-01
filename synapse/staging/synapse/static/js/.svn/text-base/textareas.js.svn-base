tinyMCE.init({
	mode : "textareas",
	//mode : "exact",
	//elements : "id_content",
	theme : "advanced",
    editor_selector : "mce_content",
	width : "754",
    height : "700",
	content_css : "/site_media/css/styles.css",
    //content_css: '/js/tiny_mce/plugins/gallerycon/css/tiny-mce-extra.css',
    jquery_url: '/js/jquery/jquery-1.4.2.min.js',
	theme_advanced_toolbar_location : "top",
	theme_advanced_toolbar_align : "left",
	theme_advanced_buttons1 : "formatselect,fullscreen,separator,preview,separator,bold,italic,separator,bullist,numlist,separator,undo,redo,separator,link,unlink,anchor,separator,gallerycon,image,separator,cleanup,help,separator,code",
	theme_advanced_buttons2 : "",
	theme_advanced_buttons3 : "",
	auto_cleanup_word : true,
	plugins : "save,preview,gallerycon,table,fullscreen,advhr,advimage,advlink,emotions,iespell,insertdatetime,searchreplace,print,contextmenu", // gallerycon connects django-photologue and TinyMCE
	plugin_insertdate_dateFormat : "%m/%d/%Y",
	plugin_insertdate_timeFormat : "%H:%M:%S",
	extended_valid_elements : "a[name|href|target=_blank|title|onclick],img[class|src|border=0|alt|title|hspace|vspace|width|height|align|onmouseover|onmouseout|name],hr[class|width|size|noshade],font[face|size|color|style],span[class|align|style]",
	fullscreen_settings : {
		theme_advanced_path_location : "top",
		theme_advanced_buttons1 : "fullscreen,separator,preview,separator,cut,copy,paste,separator,undo,redo,separator,search,replace,separator,code,separator,cleanup,separator,bold,italic,underline,strikethrough,separator,forecolor,backcolor,separator,justifyleft,justifycenter,justifyright,justifyfull,separator,help",
		theme_advanced_buttons2 : "removeformat,styleselect,formatselect,fontselect,fontsizeselect,separator,bullist,numlist,outdent,indent,separator,link,unlink,anchor",
		theme_advanced_buttons3 : "sub,sup,separator,image,insertdate,inserttime,separator,tablecontrols,separator,hr,advhr,visualaid,separator,charmap,emotions,iespell,flash,separator,print"
	},
    gallerycon_settings : {
        urls : {
            galleries : 'http://127.0.0.1:8000/photologue/galleries?format=json&jsoncallback=?',
            images : 'http://127.0.0.1:8000/photologue/images/{gallery_id}?format=json&jsoncallback=?',
            image : 'http://127.0.0.1:8000/photologue/image/{image_id}?format=json&jsoncallback=?',
            img_src : 'http://127.0.0.1:8000/photologue/image_src/{image_id}/{size_id}?format=json&jsoncallback=?'
        },
        default_size : 'thumbnail',
        default_alignment : 'left',
    }
});

// mce_editable="true"
// cols="75" rows="30" mce_editable="true"

// Multiple configs/inits
// http://tinymce.moxiecode.com/examples/example_04.php

//textareas - Converts all TEXTAREA elements to editors upon pageload.
//specific_textareas - Converts all TEXTAREA elements with the attribute "mce_editable" set to true.
//exact - Converts only explicit elements, these are listed in the "elements" setting. 
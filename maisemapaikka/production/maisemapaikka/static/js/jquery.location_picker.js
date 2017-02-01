//google.load("maps", "2");
function isEmpty( inputStr ) 
{ 
	if ( null == inputStr || "" == inputStr ) 
	{ 
		return true; 
	} 
	return false; 
}

$(document).unload(function(){
    GUnload();
});

$(document).ready(function(){
    $("input.location_picker").each(function (i) {
        var map = document.createElement('div');
        map.className = "location_picker_map";
        this.parentNode.insertBefore(map, this);
        $(this).css('display','none');
        
        var lat;
        var lng;
        
        if (isEmpty(document.getElementById("id_lat").value) || isEmpty(document.getElementById("id_lon").value))
        {
            lat = 62.236273;
            lng = 25.734673;
        } 
        else 
        {			
            lng = parseFloat(document.getElementById("id_lon").value.replace(",", "."));
            lat = parseFloat(document.getElementById("id_lat").value.replace(",", "."));
        }       
    
        var latElement = document.getElementById('id_lat');
        var lonElement = document.getElementById('id_lon');
        
        /*if (this.value.split(',').length == 2) {
            values = this.value.split(',');
            lat = values[0];
            lng = values[1];
        }*/

        //latElement.value = lat;
        //lonElement.value = lng;
        
        var map = new GMap2(map);
        map.addControl(new GSmallMapControl());
        var center = new GLatLng(62.236273, 25.734673);
        map.setCenter(center, 7);
        map.enableScrollWheelZoom();

        this.onMapClick = function(overlay, point) {
            this.value = point.lat()+','+point.lng();
            if (this.marker == null) {
                this.marker = new GMarker(point);
                this.map.addOverlay(this.marker);
            } else {
                this.marker.setPoint(point);
            }
            latElement.value = point.lat();
            lonElement.value = point.lng();
        }

        this.marker = new GMarker(new GLatLng(lat, lng));
        map.addOverlay(this.marker);
        
        latElement.value = lat;
        lonElement.value = lng;

        GEvent.bind(map, "click", this, this.onMapClick);
    });
});
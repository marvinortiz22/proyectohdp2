const input=document.getElementById('place_input');
let autocomplete
document.getElementById("id_latitud").readOnly = true;
document.getElementById("id_longitud").readOnly = true;
$(function(){
    
    if(navigator.geolocation)
    {
        navigator.geolocation.getCurrentPosition(getCoords, getError);
        initAutocomplete();
    }else{
        initialize(13.30272, -87.144107);
    }

    function getCoords(position)
    {
        var lat=position.coords.latitude;
        var lng=position.coords.longitude;

        initialize(lat, lng);
    }

    function getError(err)
    {
        initialize(13.30272, -87.144107);
    }

    function initialize(lat, lng)
    {
        var latlng = new google.maps.LatLng(lat, lng);
        var mapSettings = {
            center: latlng,
            zoom: 15,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        }

        map= new google.maps.Map($('#mapa').get(0), mapSettings);

        var marker = new google.maps.Marker({
            position: latlng,
            map: map,
            draggable: true,
        })

        google.maps.event.addListener(marker, 'position_changed',function(){
            getMarkerCoords(marker);
        })

    }

    function getMarkerCoords(marker)
    {
        var markerCoords=marker.getPosition();
        $('#id_latitud').val( markerCoords.lat());
        $('#id_longitud').val( markerCoords.lng());
    }
    
    function initAutocomplete(){
        autocomplete=new google.maps.places.Autocomplete(input);
        autocomplete.addListener('place_changed',function(){
            
            const place=autocomplete.getPlace();
            map.setCenter(place.geometry.location); 
            
            var marker = new google.maps.Marker({
                position: place.geometry.location,
                map: map,
                draggable: true,
            })  
            google.maps.event.addListener(marker, 'position_changed',function(){
                getMarkerCoords(marker);
            })    
        });
    }
})

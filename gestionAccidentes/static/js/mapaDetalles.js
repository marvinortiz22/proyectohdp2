$(function(){
    if(navigator.geolocation)
    {
        navigator.geolocation.getCurrentPosition(getCoords, getError);
    }else{
        initialize(13.30272, -87.144107);
    }

    function getCoords(position)
    {
        var lat=$('#id_latitud').val();
        var lng=$('#id_longitud').val();

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
            draggable: false,
        })

    }  
})

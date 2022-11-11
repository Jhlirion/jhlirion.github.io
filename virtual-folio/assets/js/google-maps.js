function initMap() {
    // Latitude and Longitude
    var myLatLng = {lat: -9.9295323, lng: -76.2425571};

    var map = new google.maps.Map(document.getElementById('google-maps'), {
        zoom: 17,
        center: myLatLng
    });

    var marker = new google.maps.Marker({
        position: myLatLng,
        map: map,
        title: 'South Jakarta, INA' // Title Location
    });
}
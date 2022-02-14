//Menu
$(document).ready(function () {
    $('.menu__icon').click(function () {
        $('body').toggleClass('menu_shown');
    });
});

//Map
function initMap() {
    //location
    const denver = { lat: 39.77, lng: -104.98 };
    //centered map
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 4,
        center: denver,
    });
    //marker
    const marker = new google.maps.Marker({
        position: denver,
        map: map,
    });
}
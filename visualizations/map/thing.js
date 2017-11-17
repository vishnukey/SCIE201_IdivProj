'use strict';
function initMap() {
     var map = new google.maps.Map(document.querySelector('#map'), {
         zoom: 4,
         center: {lat: 37.090, lng: -95.712},
         mapTypeId: 'terrain'
       });
       return map;
}

$(function() {
               map = initMap()
               circles = []
               $.get("/data.php",{}, function(data) {
                       console.log(data)
                       communities = data.communities
                       var community
                       for (community in communities){
                               console.log(community)
                               var circ = new google.maps.Circle({
                                       strokeColor: '#FF0000',
                                       strokeWeight: 0.8,
                                       strokeOpacity: 2,
                                       fillColor: '#FF0000',
                                       fillOpacity: 0.35,
                                       map: map
                                       center: community.location,
                                       radius: community.total
                               })
                               circles.push(circ)
                       }
               })
})

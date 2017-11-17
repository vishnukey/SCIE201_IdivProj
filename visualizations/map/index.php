<?php
$filename = "../../secrets/key";
$file = fopen($filename, "r");
$key = fread($file, filesize($filename));
fclose($file);
?>

<!DOCTYPE html>
<html lang="en">
<head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Map</title>
        <style>
              /* Always set the map height explicitly to define the size of the div
               * element that contains the map. */
              #map {
                height: 100%;
              }
              /* Optional: Makes the sample page fill the window. */
              html, body {
                height: 100%;
                margin: 0;
                padding: 0;
              }
        </style>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
</head>
<body>
        <h1>Hello, World</h1>
        <div id="map"></div>
        <script <?php echo 'src="https://maps.googleapis.com/maps/api/js?key='.$key.'">';?> > </script>
        <script>
                function initMap() {
                        var map = new google.maps.Map(document.querySelector('#map'), {
                         zoom: 11,
                         center: {lat: 51.068, lng: -114.0708},
                         mapTypeId: 'terrain'
                       });
                       return map
                }

                $(() => {/*strokeOpacity: 2,
                ,
                ,

                */
                               map = initMap()
                               circles = []
                               $.get("/data.php",{}, data => {
                                       console.log(data)
                                       communities = data.communities
                                       for (let community of communities){
                                               console.log(community)
                                               const params = {
                                                       radius: community.total / 2,
                                                       center: community.location,
                                                       map: map,
                                                       fillColor: '#FF0000',
                                                       fillOpacity: 0.35,
                                                       strokeColor: '#FF0000',
                                                       strokeWeight: 0.8,
                                                       strokeOpacity: 2
                                               }
                                               let circ = new google.maps.Circle(params)
                                               circles.push(circ)
                                       }
                               })
                })
          </script>
</body>
</html>

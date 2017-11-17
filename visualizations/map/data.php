<?php
$filename = "../../data/censusPretty_newGeom.geojson";
$file = fopen($filename, "r");
$data = fread($file, filesize($filename));
fclose($file);

header('Content-type: application/json');
echo $data;
?>

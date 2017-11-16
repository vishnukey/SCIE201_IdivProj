# What I Have Done
- downloaded data from a(src="https://data.calgary.ca/api/geospatial/cje4-zd6c?method=export&format=GeoJSON")https://data.calgary.ca/api/geospatial/cje4-zd6c?method=export&format=GeoJSON
- prettified using 
        ``` bash
        $ cat Census\ By\ Community\ 2016.geojson | python -m json.tool > censusPretty.geojson
        ```
- used regex pattern in Atom to remove geo data (TODO: write in regex pattern)
- ran python script to remove all non-residential entries 

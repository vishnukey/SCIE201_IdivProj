# What I have done
- downloaded data from a(src="https://data.calgary.ca/api/geospatial/cje4-zd6c?method=export&format=GeoJSON")https://data.calgary.ca/api/geospatial/cje4-zd6c?method=export&format=GeoJSON
- prettified using 
        ```
        $ cat Census\ By\ Community\ 2016.geojson | python -m json.tool > censusPretty.geojson
        ```
- used regex pattern in Atom to remove geo data (TODO: write in regex pattern)
- ran python script to remove all non-residential entries 

# What I need to do
- get maps API ket
- extract only people data from what I have
- geocode each community
- move data from json to csv
- do some work in excel/openRefine
- make map
- figure out other two visualizations
- write up doc

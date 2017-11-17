# What I have done
- downloaded data from a(src="https://data.calgary.ca/api/geospatial/cje4-zd6c?method=export&format=GeoJSON")https://data.calgary.ca/api/geospatial/cje4-zd6c?method=export&format=GeoJSON
- prettified using 
        ```
        $ cat Census\ By\ Community\ 2016.geojson | python -m json.tool > censusPretty.geojson
        ```
- used regex pattern in Atom to remove geo data (TODO: write in regex pattern)
- ran python script to remove all non-residential entries 
- ran python script to extract only the necessary data

# What I need to do
- get maps API ket
- geocode each community
- make map
- make pie chart: fem vs male
- make pie chart: age distribution
- write up doc

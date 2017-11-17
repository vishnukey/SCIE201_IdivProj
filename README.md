# What I have done
- downloaded data from ["https://data.calgary.ca/api/geospatial/cje4-zd6c?method=export&format=GeoJSON"](https://data.calgary.ca/api/geospatial/cje4-zd6c?method=export&format=GeoJSON)
- prettified using 
        ```
        $ cat Census\ By\ Community\ 2016.geojson | python -m json.tool > censusPretty.geojson
        ```
- used regex pattern in Atom to remove geo data (TODO: write in regex pattern)
- ran python script to remove all non-residential entries 
- ran python script to extract only the necessary data
- ran python script geocode community names using google maps api
- built php server to generate map and serve data to map
- generated map
- used R to generate pie chart for gender distribution
- used R to generate pie chart for age distribution

# What I need to do
- write up doc

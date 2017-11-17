#!/usr/bin/env python

import json
import requests

#i/o
IN_FILE_NAME = "../data/censusPretty_selectOnly.json"
OUT_FILE_NAME = "../data/censusPretty_newGeom.geojson"

#queries
API_KEY = open("../secrets/key", "r").read().rstrip()
URL = "https://maps.googleapis.com/maps/api/geocode/json?address={query}&key={key}"
QUERY_HEADER = "Calgary,+Alberta,+"

def prepRequest(text):
    community = "+".join(text.split(" "))
    query = QUERY_HEADER + community

    return URL.format(query = query, key = API_KEY)

if __name__ == "__main__":
    with open(IN_FILE_NAME, "r") as f:
        data = json.load(f)
        communities = data["communities"]
        for community in communities:
            query = prepRequest(community["name"])
            r = requests.get(query).json()
            latLng = r["results"][0]["geometry"]["location"]
            community["location"] = latLng
            #print(json.dumps(latLng, indent=4))

        outData = data
        with open(OUT_FILE_NAME, "w") as out:
            json.dump(outData, out, indent=4)

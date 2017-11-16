#!/usr/bin/env python

import json

with open("../data/censusPretty_withoutGeom.geojson", "r") as f:
    data = json.load(f)
    size = len(data["features"])
    i = 0
    while i < size:
        if data["features"][i]["properties"]["class"] != "Residential":
            del data["features"][i]
            size -= 1
            i -= 1
        i += 1
    print(size)         

    with open("../data/censusPretty_resOnly.json", "w") as out:
        json.dump(data, out, indent=4)




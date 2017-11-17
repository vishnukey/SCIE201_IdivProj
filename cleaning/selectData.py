#!/usr/bin/env python

import json

intFields = ["fem_5_14", "fem_15_19", "male_5_14", "male_15_19"]

with open("../data/censusPretty_resOnly.json", "r") as f:
    data = json.load(f)
    communityData = []
    totals = {
        "male"  : 0,
        "fem"   : 0,
        "5_14"  : 0,
        "15_19" : 0,
        "total" : 0
    }

    for blob in data["features"]:
        prop = blob["properties"]
        new = {}

        new["name"] = prop["name"]
        for field in intFields:
            new[field] = int(prop[field])

        new["total_male"]  = new["male_5_14"]  + new["male_15_19"]
        new["total_fem"]   = new["fem_5_14"]   + new["fem_15_19"]

        new["total_5_14"]  = new["male_5_14"]  + new["fem_5_14"]
        new["total_15_19"] = new["male_15_19"] + new["fem_15_19"]

        new["total"]       = new["total_male"] + new["total_fem"]

        totals["male"]  += new["total_male"]
        totals["fem"]   += new["total_fem"]
        totals["5_14"]  += new["total_5_14"]
        totals["15_19"] += new["total_15_19"]
        totals["total"] += new["total"]


        communityData.append(new)

    outData = {
        "totals"      : totals,
        "communities" : communityData
    }

    with open("../data/censusPretty_selectOnly.json", "w") as out:
        json.dump(outData, out, indent=4)

#!/usr/bin/env python

import json

fields = ["name", "fem_5_14", "fem_15_19", "male_5_14", "male_15_19"]

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

        for field in fields:
            new[field] = prop[field]

        new["total_male"]  = int(new["male_5_14"]) + int(new["male_15_19"])
        new["total_fem"]   = int(new["fem_5_14"]) + int(new["fem_15_19"])

        new["total_5_14"]  = int(new["male_5_14"]) + int(new["fem_5_14"])
        new["total_15_19"] = int(new["male_15_19"]) + int(new["fem_15_19"])

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

import pandas as pd
import jellyfish

with open("../data/station_id.csv") as f:
    w = f.readlines()

js = {}

for i in w:
    o = i.split(",")
    js[o[1]] = o[0]

def get_station_id(name):
    stations_scores = []
    for i in js.keys():
        stations_scores.append((jellyfish.jaro_similarity(i, name), js[i]))

    return max(stations_scores, key=lambda x: x[0])[1]
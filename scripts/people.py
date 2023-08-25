import csv

d = {}

with open("../data/people.csv") as f:
    r = csv.reader(f, delimiter=";")
    for i in r:
        d[int(i[0])] = i[1]

def get_people_by_station_id(attr):
    return d[attr]


import csv

stations_info = dict()
with open('data/ds_bandwidth_prepared_park.csv', newline='\n') as csvfile:
    next(csvfile)
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        if int(row[4]) not in stations_info.keys():
            stations_info[int(row[4])] = [float(row[1]), float(row[5]), float(row[6]), float(row[7]), float(row[8]), float(row[9]), float(row[10])]
        else:
            stations_info[int(row[4])][1] += float(row[5])
            stations_info[int(row[4])][2] += float(row[6])
            stations_info[int(row[4])][3] += float(row[7])
            stations_info[int(row[4])][4] += float(row[8])
            stations_info[int(row[4])][6] += float(row[10])


import os
import csv
DATADIR = ""
DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
    data = []
    n = 0
    with open(datafile, "r") as f:
        r = csv.DictReader(f)
        for row in r:
            print(row['Title'], row['Released'])
        # for line in r:         
        #     data.append(line)
    return data

if __name__ == '__main__':
    datafile = os.path.join(DATADIR, DATAFILE)
    parse_file(datafile)
    d = parse_file(datafile)
    print(d)

    
# test()
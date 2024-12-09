# CSV - comma sep file

import csv

with open("TestData2.csv") as csvfile:
    reader = csv.reader(csvfile)
    for col in reader:
        print(col[0], col[1], sep="|")
import csv
import os

f = open('budget_data.csv')

csv_f = csv.reader(f)

for row in csv_f:
    print (row)


#f.close()



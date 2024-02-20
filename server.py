import sys
import os
from customer import Customer


if len(sys.argv) < 2:
    print("Error: missing csv file name!")
    quit()

csv_file = sys.argv[1]
if not os.path.exists(csv_file):
    with open(csv_file, "w"):
        pass

customers = []
with open(csv_file, "r") as fd:
    for line in fd.readlines():
        fields = line.split(",")
        index = -1
        id = int(fields[2])
        for i, Customer in enumerate(customers):
            if Customer.id == id:
                index = i
                break
        if index >= 0:
            customers[]




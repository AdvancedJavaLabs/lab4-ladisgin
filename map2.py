#!/usr/bin/python3
import sys
import csv

for line in sys.stdin:
    line = line.strip()
    category, revenue, quantity = line.split("\t")
    print(str(category) + "\t" + str(revenue) + "\t" + str(quantity))

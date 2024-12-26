#!/usr/bin/python3
import sys
import csv

def parse_csv_line(line):
    try:
        fields = list(csv.reader([line]))[0]
        return fields
    except:
        return None

for line in sys.stdin:
    line = line.strip()
    if line.startswith("transaction_id"):
        continue
    fields = parse_csv_line(line)
    if fields:
        _, _, category, price, quantity = fields
        revenue = float(price) * int(quantity)
        print(str(category) + "\t" + str(revenue) + "\t" + str(quantity))

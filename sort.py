#!/usr/bin/python3
import sys

data = []
for line in sys.stdin:
    category, revenue, quantity = line.strip().split("\t")
    revenue = float(revenue)
    quantity = int(quantity)
    data.append((category, revenue, quantity))

data.sort(key=lambda x: x[1], reverse=True)

print("Category\tRevenue\tQuantity")
for category, revenue, quantity in data:
    print(str(category) + "\t" + str(revenue) + "\t" + str(quantity))

#!/usr/bin/python3
import sys

current_category = None
total_revenue = 0.0
total_quantity = 0

for line in sys.stdin:
    line = line.strip()
    category, revenue, quantity = line.split("\t")
    revenue, quantity = float(revenue), int(quantity)
    
    if category != current_category:
        if current_category:
            print(str(current_category) + "\t" + str(total_revenue) + "\t" + str(total_quantity))
        current_category = category
        total_revenue = 0.0
        total_quantity = 0
    
    total_revenue += revenue
    total_quantity += quantity

if current_category:
    print(str(current_category) + "\t" + str(total_revenue) + "\t" + str(total_quantity))

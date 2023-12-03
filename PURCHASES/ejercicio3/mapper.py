#!/usr/bin/python

import sys

for line in sys.stdin:
    try:
        data = line.strip().split("\t")
        date, time, store, item, cost, payment = data
        print(payment + "\t" + cost)
    except ValueError:
        continue


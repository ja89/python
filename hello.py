#!/usr/bin/env python3.6

firstArray = ['tom', 'harry', 'john']
secondArray = ['tom', 'john', 'tony']
for i in firstArray:
    for l in secondArray:
        if i == l:
            print(i)
        else:
            continue

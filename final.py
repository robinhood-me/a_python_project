


#! /usr/bin/python3
from typing import List
import sys

data = {'red': [['y', 'x'], ['b', 'a'], ['e', 'd']],
        'yellow': [['u', 't'], ['j', 'i'], ['m', 'l']],
        'blue': [['s', 'r'], ['r', 'q'], ['z', 'y']]}

sorted_keys = sorted ( data.keys() )

for k in sorted_keys:
    for inner_list in data[k] :
        inner_list.sort()
    data[k].sort()

for k in sorted_keys:
    print(f"{k}: {data[k]}")
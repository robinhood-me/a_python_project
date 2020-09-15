#! /usr/bin/ python3
from typing import List
import sys

data = {'red': [['y', 'x'], ['b', 'a'], ['e', 'd']],
        'yellow': [['u', 't'], ['j', 'i'], ['m', 'l']],
        'blue': [['s', 'r'], ['r', 'q'], ['z', 'y']]}

sorted_keys = sorted ( list ( data.keys() )  )

for k in sorted_keys:
    # data[k] is what you have been calling an outer loop
    assert isinstance(data[k], list), f"data[{k}] should be a list, but it's actually a {type(data[k])}. {data[k]}"
    for ol in data[k] :
        # ol is both an element of the outer list and a list in its own right
        assert isinstance(ol, list), f"ol should be a list, but it's actually a {type(ol)}. {ol}"
        ol.sort()
    data[k].sort()

for k in sorted_keys:
    print(f"{k}: {data[k]}")
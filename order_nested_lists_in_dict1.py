data = {'red': [['y', 'x'], ['b', 'a'], ['e', 'd']],
        'yellow': [['u', 't'], ['j', 'i'], ['m', 'l']],
        'blue': [['s', 'r'], ['r', 'q'], ['z', 'y']]}

newDict={}
"""
sorted_keys = sorted ( list ( data.keys() ) )
sorted_values = sorted ( list ( data.values() ) )
print(sorted_keys, sorted_values)
#for key in sorted_keys.keys():  # reaching the keys of the dictionary
#    print(key)
"""

for key, value in sorted(data.items()), key = lambda r: r[1][2][3]):
    print(key, value)

"""
desired output

{'blue': [['q', 'r'], ['r', 's'], ['y', 'z']],
 'red': [['a', 'b'], ['d', 'e'], ['x', 'y']],
 'yellow': [['i', 'j'], ['l', 'm'], ['t', 'u']]}
"""
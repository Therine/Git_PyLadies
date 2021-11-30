colours = {
    'pear': 'green',
    'apple': 'red',
    'melon': 'green',
    'plum': 'purple',
    'radish': 'red',
    'cabbage': 'green',
    'carrot': 'orange',
}

colour_riped = dict(colours)
for key in colour_riped:
    colour_riped[key] = 'dark-brown-'+ colour_riped[key]
print(colour_riped)
phones = {
    'Tyna': '153 85283',
    'Lubo': '237 26505',
    'Andreea': '385 11223',
    'Fabian': '491 88047',
    'Vitoria': '491 88047',
    'Oliwia': '491 88047',
}

#for person in phones:
 #   phones[person] = f'+43{phones[person]}'
#print(phones)
#keys_to_delete = ['Lubo', 'Tyna', 'Oliwia']
#for key in phones:
#    if key == keys_to_delete:
#        del key
#    else:
#        print(key)
    
print(phones)

keys_to_delete = ['Lubo', 'Tyna', 'Oliwia']
for key_to_del in keys_to_delete:
    del phones[key_to_del]
print(phones)
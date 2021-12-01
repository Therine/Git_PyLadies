#Print out following information about each user of they have it: His/her 'username', 'full name' (first and last with first letter capitalized), 'email', 'city' they live in and 'country' they live in
users = {
  'aeinstein': {
    'first': 'albert',
    'last': 'einstein',
    'location': 'princeton',
    'email': 'albgenious1@princeton.org',
  },
  'mcurie': {
    'first': 'marie',
    'last': 'curie',
    'location': 'paris',
  },
}

cities = {
  'paris': {
    'country': 'France',
    'population': 2161,
  },
  'london': {
    'country': 'Great Britain',
    'population': 8960,
  },
  'princeton': {
    'country': 'United States of America',
    'population': 28,
  }
}
#print(users)
#print(cities)
for item in users:
    Username = users[item]
    print (Username)
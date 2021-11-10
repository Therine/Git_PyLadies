# This program gives naive life advice.

print('Answer "yes" or "no".')
happy_status = input('Are you happy?')
if happy_status == 'yes':
    happy = True
elif happy_status == 'no':
    happy = False
else:
    print('I do not understand!')

rich_status = input('Are you rich?')
if rich_status == 'yes':
    rich = True
elif rich_status == 'no':
    rich = False
else:
    print('I do not understand!')

if rich and happy:
    # rich and at the same time.
    print('Congratulations!')
elif rich:
    # rich but not "rich and happy",
    #so must be only rich.
    print('Try to smile more.')
elif happy:
    # must be only happy.
    print('Try to spend less.')
else:
    # neither happy nor rich.
    print("I'm sorry for you.")
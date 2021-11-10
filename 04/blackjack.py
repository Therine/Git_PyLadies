from random import randrange

sum = 0

print ('You have 0 points')
while sum < 21:
    response = input('Do you want to continue? ')
    if response == 'yes':
        print ('Computer turns a card over.')
        card = randrange(2,11)
        print('Your card value is', card)
        sum = sum + card
    elif response == 'no':
        print("You can't win if you don't play. Your point total was", sum, "when you decided to quit.")
        break
    else:
        print("I only understand yes or no. Sorry")

if sum == 21:
    print('Congratulations! You won!')
elif sum > 21:
    print('Bad luck!', sum, 'points is too much!')
else:
    print('So close! You missed', 21 - sum, 'points!')
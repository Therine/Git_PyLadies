#lists are used to store different items in one variable.
#lists start with square brackets []
numbers = [1, 1, 2, 3, 5, 8, 13]
print(numbers)

for number in numbers:
    print(number)


numbers = [1, 0, 3, 4]
numbers[1] = 2
print(numbers)

deck = []
for color in '♠', '♥', '♦', '♣':
    for value in list(range(2, 11)) + ['J', 'Q', 'K', 'A']:
        deck.append(str(value) + color)
print(deck)


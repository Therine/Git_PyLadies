with open ("input_04-dec.txt") as f:
    #lines = f.read().splitlines()
    lines = f.read().split()
#change the strings into integers
#for i in range(0, len(lines)):
#    lines[i] = int(lines[i])
#print(lines)
#print(lines[0])
drawn_numbers = lines[0].split(',')
cards = lines[1:2501]
#space = rows[0].split(' ')
print(cards)
#something that can store the space of the card and whether it have been drawn
#print(boards)
#print(drawn_numbers)
# we need to iterate through the drawn_numbers list to mark each number that comes up. 
# I need to define what it means to get Bingo
# Like, if indexes in groups of 5 are marked () = bingo
# if indexes in multiples of 5 are marked 
#for i in boards:
#    if i == drawn_numbers[int(i)]:
#        i.append('x')

#print(boards)

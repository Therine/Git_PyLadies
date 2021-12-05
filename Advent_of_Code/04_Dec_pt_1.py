with open ("input_04-dec.txt") as f:
    #lines = f.read().splitlines()
    lines = f.read().split()
#change the strings into integers
#for i in range(0, len(lines)):
#    lines[i] = int(lines[i])
#print(lines)
#print(lines[0])
drawn_numbers = lines[0].split(',')
boards = lines[1:2501]
#print(boards)
print(drawn_numbers)
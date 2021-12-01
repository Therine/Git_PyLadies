#How many measurements are larger than the previous measurement?
#Code from Tyna to use the data in the file that I downloaded from Advent of Code
with open ("input.txt") as f:
    lines = f.read().splitlines()

#prestep, can I even find the difference between 2 of these items in the lines list?
difference = int(lines[1]) - int(lines[0])
print(difference)
#First, I need to iterate over each measurement in order to calculate the difference
#for i in lines:
#    difference = i - lines[:1]
#    print(difference)

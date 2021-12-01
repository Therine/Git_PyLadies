#How many measurements are larger than the previous measurement?
#Code from Tyna to use the data in the file that I downloaded from Advent of Code
with open ("input.txt") as f:
    lines = f.read().splitlines()
    #This data is a set of strings right now
    for i in range(0, len(lines)):
        lines[i] = int(lines[i])
#hopefully it isn't a set of strings?
print(lines)

#prestep, can I even find the difference between 2 of these items in the lines list?
#difference = int(lines[1]) - int(lines[0])
#print(difference)
#A really bizarre way to figure this out is to make one more list from these files and just compare each index against each other. 
#difference = []
#First, I need to iterate over each measurement in order to calculate the difference
#for i in lines:
    #difference = int(lines[:-1]) - int(lines[1:])
    #print(difference)

#idea found here: https://stackoverflow.com/questions/2400840/python-finding-differences-between-elements-of-a-list
#result = [j-i for i, j in zip(int(lines[:-1]), int(lines[1:]))]
# I can't get it to run!


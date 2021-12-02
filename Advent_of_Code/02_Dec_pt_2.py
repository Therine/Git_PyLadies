from turtle import forward, up, down, exitonclick
#Code from Tyna to use the data in the file that I downloaded from Advent of Code
with open ("input_02_dec.txt") as f:
    #lines = f.read().splitlines()
    lines = f.read().split()
for i in range(1, len(lines), 2):
    lines[i] = int(lines[i])
#print(lines)

#Calculate the horizontal position and depth you would have after following the planned course. 
#What do you get if you multiply your final horizontal position by your final depth?
#Sum up all of the forward numbers, easy enough
#
#horizontal = sum(lines)
#ran into the str versus int issue
horizontal = 0
depth = 0
aim = 0
for i in range(0, len(lines)):
    if lines[i] == 'forward':
        horizontal = horizontal + int(lines[i+1])
        depth = depth + (int(lines[i+1]) * aim)
    if lines[i] == 'up':
        #depth = depth - int(lines[i+1])
        aim = aim - int(lines[i+1])
    if lines[i] == 'down':
        #depth = depth + int(lines[i+1])
        aim = aim + int(lines[i+1])
#    else:
#        break
#This loop is looking for forward elements to extract the number and add them all together
#for step in lines:
#    if step 
print(horizontal)
print(depth)
print(aim)
print(horizontal*depth)
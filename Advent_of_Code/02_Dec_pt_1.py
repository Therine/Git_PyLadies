from turtle import forward, up, down, exitonclick
#Code from Tyna to use the data in the file that I downloaded from Advent of Code
with open ("input_02_dec.txt") as f:
    lines = f.read().splitlines()


print(lines)
#Calculate the horizontal position and depth you would have after following the planned course. 
#What do you get if you multiply your final horizontal position by your final depth?
#Sum up all of the forward numbers, easy enough
#
horizontal = 0
depth = 0

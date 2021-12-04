#Code from Tyna to use the data in the file that I downloaded from Advent of Code
with open ("input_03_dec.txt") as f:
    #lines = f.read().splitlines()
    lines = f.read().split()
#change the strings into integers
#for i in range(0, len(lines)):
#    lines[i] = int(lines[i])
#print(lines)
#print(len(lines))
#print(len(lines[0]))
bit_position = []

ogr_list = []

#Next, you should verify the life support rating, 
#which can be determined by multiplying the oxygen 
#generator rating by the CO2 scrubber rating.
#Start with all 1000 numbers in the lines list
#To calculate the oxygen regulator rating:
#Evaluate which is the most common bit (1 or 0) in lines[0] 
#Append the original element from lines if the first bit is most common to the ogr_list
#Use the ogr_list for all subsequent bit evaluations

for i in range(len(lines)):
    
    bit = lines[i][0]
    bit_position.append(bit)

#len(lines) = 1000
#len(lines[0]) = 12
##change the strings into integers 
for j in range(0, len(bit_position)):
    bit_position[j] = int(bit_position[j])

if sum(bit_position) >= 500:
    ogr_list.append(lines[i])
        
bit_position = []




print(ogr_list)

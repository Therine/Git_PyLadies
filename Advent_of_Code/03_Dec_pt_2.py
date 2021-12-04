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

complete_ogr = []
ogr_list = []
ogr_list2 = []  #This is where I'm going to put my first set after the line[0] bits are evaluated. 
#And then use this to put the next set for ogr_list[1]


#Next, you should verify the life support rating, 
#which can be determined by multiplying the oxygen generator rating by the CO2 scrubber rating.
#Start with all 1000 numbers in the lines list
#To calculate the oxygen regulator rating:
#Evaluate which is the most common bit (1 or 0) in lines[0] 
#Append the original element from lines if the first bit is most common to the ogr_list
#Use the ogr_list for all subsequent bit evaluations
#I need a function that takes the 1000 elements and creates the sublist of elements that coorespond to the most common bit
def MCVariable(eval_list,idx):
    for i in range(0,len(eval_list)):
        if eval_list[i][idx] == 1:
            ogr_list.append(eval_list[i])
        if eval_list[i][idx] == 0:
            ogr_list2.append(eval_list[i])
    if len(ogr_list) >= 500:
        complete_ogr.append(ogr_list)
    else:
        complete_ogr.append(ogr_list2)
    return complete_ogr
MCVariable(lines,0)
for idx in range(0,12):
    MCVariable(complete_ogr,idx)



print(len(ogr_list))
print(ogr_list)
print(complete_ogr)

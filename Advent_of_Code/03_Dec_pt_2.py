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
complete_co2 = []
ogr_list2 = []  #This is where I'm going to put my first set after the line[0] bits are evaluated. 
#And then use this to put the next set for ogr_list[1]


#Next, you should verify the life support rating, 
#which can be determined by multiplying the oxygen generator rating by the CO2 scrubber rating.
#Start with all 1000 numbers in the lines list
#To calculate the oxygen regulator rating:
#Evaluate which is the most common bit (1 or 0) in lines[0] 
#Append the original element from lines if the first bit is most common to the ogr_list
#Use the ogr_list for all subsequent bit evaluations, so there are 516 elements for line[1]
#I need a function that takes the 1000 elements and creates the sublist of elements 
# that coorespond to the most common bit
def MCBit(eval_list,idx):
    list1 = []
    list0 = []
    
    for i in range(0,len(eval_list)):
        if eval_list[i][idx] == '1':
            list1.append(eval_list[i])
        if eval_list[i][idx] == '0':
            list0.append(eval_list[i]) 
    #print(len(list1), '<= length of the ones that start with 1')
    #print(len(list0), '<= length of the ones that start with 0')
    if len(list1) >= len(list0):
        return list1
    if len(list1) < len(list0):
        return list0
        
    #len(lines) = 1000
    #len(lines[0]) = 12
    
    #it needs to got through and evaluate each element of lines 
    # in order to populate the ogr_list properly
def LCBit(eval_list,idx):
    list1 = []
    list0 = []
    
    for i in range(0,len(eval_list)):
        if eval_list[i][idx] == '1':
            list1.append(eval_list[i])
        if eval_list[i][idx] == '0':
            list0.append(eval_list[i]) 
    #print(len(list1), '<= length of the ones that start with 1')
    #print(len(list0), '<= length of the ones that start with 0')
    if len(list1) == 0:
        return list0
    if len(list0) == 0:
        return list1
    if len(list1) >= len(list0):
        return list0
    if len(list1) < len(list0):
        return list1
  
complete_ogr = lines
complete_co2 = lines
for p in range(0,12):        
    complete_ogr = MCBit(complete_ogr,p)
    complete_co2 = LCBit(complete_co2,p)
    #print('ogr', len(complete_ogr))


#print(lines[0][0])
#print(len(ogr_list))

#print(ogr_list)
print(complete_ogr)
print(complete_co2)
ogr_rating = ''.join(map(str,complete_ogr))
int(ogr_rating)
binary_string_ogr = ogr_rating

try:
    ogr_rating_decimal = int(binary_string_ogr,2)    

except ValueError:
    print("Invalid binary number")

co2_rating = ''.join(map(str,complete_co2))
int(co2_rating)
binary_string_co2 = co2_rating

try:
    co2_rating_decimal = int(binary_string_co2,2)    

except ValueError:
    print("Invalid binary number")
print(ogr_rating_decimal)
print(co2_rating_decimal)
print(ogr_rating_decimal * co2_rating_decimal)
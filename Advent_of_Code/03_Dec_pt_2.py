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
    ogr_list = []
    bit_position = [] #This is how I'm going to examine the bit in each position 0-11. Take the sum
    # of this list and because it is binary, you can calculate the most common by whether the sum is more than 500
    for i in range(0,len(eval_list)):
        bit = eval_list[i][idx]
        bit_position.append(bit)   

    #len(lines) = 1000
    #len(lines[0]) = 12
    for j in range(0,len(bit_position)):
        bit_position[j] = int(bit_position[j])
    if sum(bit_position) >= (len(complete_ogr))/2:
    #it needs to got through and evaluate each element of lines 
    # in order to populate the ogr_list properly
        #print(sum(bit_position))
        most_frequent_bit = '1'
        for k in range (0,len(eval_list)):
            if eval_list[k][idx] == most_frequent_bit:
                ogr_list.append(eval_list[k])
    if sum(bit_position) < (len(complete_ogr))/2:
        #print(sum(bit_position))
        most_frequent_bit = '0'
        for q in range (0,len(eval_list)):
            if eval_list[q][idx] == most_frequent_bit:
                ogr_list.append(eval_list[q]) 
          
    bit_position = []
    return ogr_list

def LCBit(eval_list,idx):
    co2_list = []
    co2_list1 = []
    co2_list0 = []
    #bit_position = [] #This is how I'm going to examine the bit in each position 0-11. Take the sum
    # of this list and because it is binary, you can calculate the most common by whether the sum is more than 500
    for r in range(0,len(eval_list)):
        if eval_list[r][idx] == '1':
            co2_list1.append(eval_list[r])
            
        if eval_list[r][idx] == '0':
            co2_list0.append(eval_list[r])
            
    print(len(co2_list1), '<= the elements with the 1')
    print(len(co2_list0), '<= the elements with the 0')
    #len(lines) = 1000
    #len(lines[0]) = 12
    
    if len(co2_list1) < (len(complete_co2))/2:
    #it needs to got through and evaluate each element of lines 
    # in order to populate the co2_list properly
        co2_list.append(co2_list1)
    if len(co2_list0) < (len(complete_co2))/2:
        co2_list.append(co2_list0)
    
    return co2_list 
    
#for m in range(0,12):
#print(len(MCBit(lines,0)))
#MCBit(ogr_list,1)
#print(len(ogr_list))   
complete_ogr = lines
complete_co2 = lines
for p in range(0,12):
    complete_ogr = MCBit(complete_ogr,p)
    complete_co2 = LCBit(complete_co2,p)
    print('ogr', len(complete_ogr))
    print('co2', len(complete_co2))
    print(len(complete_ogr)+len(complete_co2))
    

#print(lines[0][0])
#print(len(ogr_list))

#print(ogr_list)
print(complete_ogr)
print(complete_co2)

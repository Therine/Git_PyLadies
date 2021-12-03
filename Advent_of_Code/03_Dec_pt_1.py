#Code from Tyna to use the data in the file that I downloaded from Advent of Code
with open ("input_03_dec.txt") as f:
    #lines = f.read().splitlines()
    lines = f.read().split()
#change the strings into integers
#for i in range(0, len(lines)):
#    lines[i] = int(lines[i])
#change the strings into integers
#for i in range(0, len(lines)):
#    lines[i] = int(lines[i])
#print(lines)
#print(len(lines))
#print(len(lines[0]))
gamma_position = []


gamma_list = []
epsilon_list = []
gamma_rate = sum(gamma_list)
epsilon_rate = sum(epsilon_list)
#power_consumption = gamma_rate * epsilon_rate
#Each bit in the gamma rate can be determined by finding 
#the most common bit in the corresponding position of all 
#numbers in the diagnostic report.
for j in range(0,12):
    for i in range(len(lines)):
        
        gamma_bit = lines[i][j]
        gamma_position.append(gamma_bit)
        print(gamma_bit)
    #The epsilon rate is calculated in a similar way; rather than use the most common bit, 
    #the least common bit from each position is used. 
    #len(lines) = 1000
    #len(lines[0]) = 12
    ##change the strings into integers
    for i in range(0, len(gamma_position)):
        gamma_position[i] = int(gamma_position[i])
    #translate the binary of gamma_rate into decimal
    #print(gamma_position)
    print(sum(gamma_position))
    if sum(gamma_position) > 500:
        gamma_list.append(1)
    if sum(gamma_position)<=500:
        gamma_list.append(0)
    gamma_position = []


print(gamma_list)
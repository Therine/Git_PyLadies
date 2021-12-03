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

gamma_list = []
epsilon_list = []

#power_consumption = gamma_rate * epsilon_rate
#Each bit in the gamma rate can be determined by finding 
#the most common bit in the corresponding position of all 
#numbers in the diagnostic report.
for i in range(0,len(lines[0])):
    gamma_bit = sum(lines[i])
    print(gamma_bit)
#The epsilon rate is calculated in a similar way; rather than use the most common bit, 
#the least common bit from each position is used. 
#len(lines) = 1000
#len(lines[0]) = 12
#
#for i in range(0,11):
#    if sum(lines[i]) > 500:
#        bit_of_gamma = 1
#        gamma_rate.append(bit_of_gamma)
#translate the binary of gamma_rate into decimal

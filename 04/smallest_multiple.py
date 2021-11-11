modulo_set = [] # the smallest number that is divisible by each number up to and including range_stop

smallest_multiple = 1
active = True

while active != False:
    factor_count = 18 # the number of factors that should be divisible
#while len(modulo_set) != factor_count and sum(modulo_set) != 0:  
    for i in range (1,factor_count): # I want to put this inside of another for loop, but I don't want to define the range stop of that one. I want the while loop to control when we stop checking divisors
        smallest_multiple_candidate = 1
        modulo = smallest_multiple_candidate % i # smallest multiple iterates by one whole number each loop. 
        modulo_set.append(modulo) # this is how you collect the 0 to evaluate whether all of the iterations divide evenly.
        smallest_multiple = smallest_multiple_candidate + 1
        print (len(modulo_set))
        if len(modulo_set) == factor_count:
            active = False
                
   

print ('factor count:', factor_count)
print ('sum of modulo set: ', sum(modulo_set))
print ('length modulo set: ', len(modulo_set))
print (active)
print (modulo_set)
print ('This should be the smallest multiple of the factorals: ', smallest_multiple)

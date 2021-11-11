modulo_set = [] # the smallest number that is divisible by each number up to and including range_stop
factor_count = 10 # the number of factors that should be divisible
smallest_multiple = 1
while True: # the first smallest multiple have have all 0 in their modulo set.:  
    for i in range (1,factor_count): # I want to put this inside of another for loop, but I don't want to define the range stop of that one. I want the while loop to control when we stop checking divisors
        smallest_multiple_candidate = 1
        modulo = smallest_multiple_candidate % i # smallest multiple iterates by one whole number each loop. 
        modulo_set.append(modulo) # this is how you collect the 0 to evaluate whether all of the iterations divide evenly.
        smallest_multiple = smallest_multiple_candidate + 1

print (sum(modulo_set))
print (modulo_set)
print (smallest_multiple)

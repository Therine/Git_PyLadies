#pyladies advice
#I would just naively go through numbers starting from 1 and test if it is divisible by prime numbers from 2 to 20 without a remainder. It will take quite some time for 1-20 but will finish eventually.
modulo_set = [] # the smallest number that is divisible by each number up to and including range_stop


factor_count = 10 # the number of factors that should be divisible

#while sum(modulo_set) != 0: # the first smallest multiple have have all 0 in their modulo set.:  
for j in range(1000):
  
  for i in range (1,factor_count): # I want to put this inside of another for loop, but I don't want to define the range stop of that one. I want the while loop to control when we stop checking divisors
      
      smallest_multiple = j
      modulo = smallest_multiple % i # smallest multiple iterates by one whole number each loop. 
      modulo_set.append(modulo) # this is how you collect the 0 to evaluate whether all of the iterations divide evenly.
    
      #smallest_multiple = smallest_multiple + 1
      modulo_set = []
  

print (sum(modulo_set))
print(modulo_set)

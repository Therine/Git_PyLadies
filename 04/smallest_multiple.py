#pyladies advice
#I would just naively go through numbers starting from 1 and test if it is divisible by prime numbers from 2 to 20 without a remainder. It will take quite some time for 1-20 but will finish eventually.
modulo_set = [] # this is the evaluation set where i divides into each smallest_multiple, and appends the modulo to this set. 
zero_set = [] # when the sum of the modulo_set equals zero, append it to this set

#factor_count = 10 # the number of factors that should be divisible
smallest_multiple = 2520
for i in range (1,10):
  modulo = smallest_multiple % i
  modulo_set.append(modulo)
  print (i)
  print(modulo_set)
  print (sum(modulo_set)) #each of these zeros represents an iteration from 1-2520 % i until the set equals zero

    


#print (sum(modulo_set))
#print(modulo_set)

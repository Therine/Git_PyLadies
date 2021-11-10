# https://www.reddit.com/r/learnprogramming/comments/lj7kh6/feedback_on_my_prime_number_finder_code/
import math

nthnumber = int(input("which nth prime are you looking for? "))
prime_list = []
while nthnumber >= len(prime_list):
  modulo_list = []
  
  #if nthnumber != len(prime_list):
  for i in range(2,100):  # the range of integers to iterate through to find prime numbers
      
      for j in range(2, int(math.sqrt(i) + 1)):  # the range of modulo numbers to iterate through.
          modulo_list.append(i % j)  # the list of modulo results, per i (range j)
      if 0 not in modulo_list:
          prime_list.append(i)  # if no zero is found in the modulo list, it's a prime number, and added to the prime_list
      modulo_list = []  # modulo list is clear for the next iteration of i (range j) modulo numbers 

print(prime_list)
nthprime = prime_list[nthnumber-1]
print(len(prime_list))
print(nthprime)
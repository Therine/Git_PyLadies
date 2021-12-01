least_common_multiple_of_numbers = 20  # change this to any positive whole number
###
# The least common multiple (LCM) of two or more numbers is the smallest number
# (not counting 0) which is a multiple of all of the numbers.
###
# ​
def brute_force_method(numbers_to_multiply=10):
    """
    Brute force example of LCM (we just increment the values by 1 and test if our condition works
    works fine for smaller numbers
    for number_of_numbers_to_multiply = 20, it already takes too long (2 minutes on my PC) - we could take a mathematical approach)
    Args:
        numbers_to_multiply (int, optional): Name of bucket. Defaults to 10.
    """
    
    smallest_multiple_candidate = 0  # variable that we shall be increasing in order to find the least common multiple
    while True:
        is_divisible_by_all = True
        smallest_multiple_candidate += 1
        # iterating over numbers of which we want to find the least_common_multiple
        # when dividing the target number by i
        for i in range(1, numbers_to_multiply + 1):
            # get a remainder of division of our candidate number and i
            remainder = smallest_multiple_candidate % i
            if remainder != 0:
                # remainder is not 0, no need to check all "i" in range, instead break to save time
                is_divisible_by_all = False
                break
        # just a progress counter of our script to know if we are in some infinite loop or not
        if smallest_multiple_candidate % 10000 == 0:
            print("Progress counter:", smallest_multiple_candidate)
        if is_divisible_by_all:
            break  # we have found out that all remainders are 0, end script
    return smallest_multiple_candidate


print("Result of brute-force method:", brute_force_method(least_common_multiple_of_numbers))
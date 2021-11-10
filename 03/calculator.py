import operator

#define operators you wanna use
allowed_operators={
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv}

#sample variables
first_number = float(input("Let's build an equation, enter in the first number: "))
user_op = input("Great, enter in the operator you what to use : '+', '-', '*' or '/': ")
second_number = float(input("Fantabulus, enter in the second number: "))

#sample calculation => a+b

solution = allowed_operators[user_op](first_number,second_number)

print("So, here's what we have: ", first_number, user_op, second_number)
print('and the solution is......', solution)
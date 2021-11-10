# This code will calculate the perimeter and area of a square, as long as you know the side length.
side = float(input('Enter the side of your square in centimeters: '))

positive_number = side > 0
if positive_number == True:
    print("The perimeter of a square with a side of", side, "cm is", 4 * side,"cm.")
    print("The area of a square with a side of", side, "cm is", side**2,"cm2.")
else:
    print("The side must be a positive number!")

print("Thank you for using the geometric calculator")
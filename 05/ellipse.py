from math import pi

def ellipse_area(length1, length2):
    "Returns the area of an ellipse, given the length of each of the axes"
    return pi * length1 * length2

print('Ellipse Area in cm2: {:0.4f}'.format(ellipse_area(10, 17)))

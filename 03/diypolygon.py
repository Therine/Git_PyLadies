from turtle import forward, pen, right,left, exitonclick, penup, pendown

side_number = int(input("Let's make a polygon. how many sides would you like? "))
outer_angle = 360/side_number
for j in range(side_number):
    forward(50)
    right (outer_angle)


    
exitonclick()
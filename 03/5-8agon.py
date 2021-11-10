from turtle import forward, pen, right,left, exitonclick, penup, pendown

outer_angle = 360/5
for j in range(5):
    forward(50)
    right (outer_angle)
print(outer_angle)

#this one draws a star!
#inner_angle = 2*((180*5-360)/5)
#for j in range(5):
  #  forward(50)
 #   left(inner_angle)
#print(inner_angle)
     
penup()
forward (50)
left (90)
pendown()
outer_angle = 360/6
for j in range(6):
    forward(50)
    right (outer_angle)
print(outer_angle)
penup()
forward (50)
left (90)
pendown()
outer_angle = 360/7
for j in range(7):
    forward(50)
    right (outer_angle)
print(outer_angle)
penup()
forward (50)
left (90)
pendown()
outer_angle = 360/8
for j in range(8):
    forward(50)
    right (outer_angle)
print(outer_angle)

#penup()
#forward (50)
#right (90)
#pendown()
    
exitonclick()
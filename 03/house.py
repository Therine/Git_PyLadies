from turtle import forward, right,left, exitonclick, penup, pendown
from math import sqrt

for j in range(3):
    forward(50)
    left (120)
right (90)
forward (50)
left (135)
forward (sqrt(50**2+50**2))
right (225)
forward (50)
left (135)
forward (sqrt(50**2+50**2))
right (225)

forward (50)
for i in range (3):
    left (90)
    forward (50)


#for i in range (1):
 #   for k in range (3):
  #      forward (sqrt(50**2+50**2))
   #     left (135)
    

exitonclick()
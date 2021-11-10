from turtle import forward, pen, right,left, exitonclick, penup, pendown
#Fibonacci number sequence 

side = float(input("pick an number between 10 and 20: "))
for i in range(30):
    right(90)
    forward(side)
    
    side = side +10


    
exitonclick()
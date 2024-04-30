#Artan Rama

#April 8 2024

#Write a turtle graphics programs that draws a triangle and a square using loops.

import turtle

square=turtle.Turtle()
for i in range(4):
    square.forward(90)
    square.right(90)

import turtle

triangle=turtle.Turtle()
for i in range(3):
    triangle.left(120)
    triangle.forward(100)
    triangle.forward(100)
    

turtle.done()    
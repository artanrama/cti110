#Artan Rama

#April 7 2024

#Write a turtle graphics programs that draws your initials.

import turtle

initials=turtle.Turtle()


for i in range(1):
    initials.penup()
    initials.goto(-50, 0)
    initials.pendown()
    initials.color("purple")
    initials.left(75)
    initials.forward(100)
    initials.right(150)
    initials.forward(100)
    initials.backward(50)
    initials.right(105)
    initials.forward(36)
    initials.penup()
    initials.goto(50,0)
    initials.pendown()
    initials.left(90)
    initials.forward(100)
    initials.backward(100)
    initials.circle(40, -360)
    initials.right(-200)
    initials.backward(90)
    

turtle.done()

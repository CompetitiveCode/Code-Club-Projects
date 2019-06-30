#!/bin/python3

from turtle import * #To import the draw functions
from random import randint #To import the random numbers function

speed(0) #This initialises the speed to max. We can also give it any number to adjust the speed
penup() #To make sure that it does not start writing from the beginning it moves.

goto(-140,140) #Almost top left portion

for i in range(15): #To draw the racing ground and also the numbers
    write(i, align='center') #To align the numbers with the lines, by default it is left aligned.
    right(90) #To turn right by 90 degree
    forward(10) #To move 10 pixels forward
    pendown() #Now we need to draw the lines
    for j in range(16): #This for loop is for dashed lines in the track
        forward(10)
        if(j%2==0): #This if statement helps for the dashed lines
            penup()
        else:
            pendown()
    penup()
    backward(170) #This is to go back, in this case, retrace.
    left(90) #This is to turn left by 90 degree
    forward(20)
    
a=Turtle() #This is our first contender
a.color('red') #This specifies the colour
a.shape('turtle') #This specifies the shape
a.penup()
a.goto(-160,110) #Starting point of the race
a.pendown()

for roll in range(4): #This is just to do a barrel roll as it reaches the starting point
    a.right(90)

b=Turtle()
b.color('blue')
b.shape('turtle') #You can also add different shapes like arrow, circle, square, triangle or classic
b.penup()
b.goto(-160,80)
b.pendown()

for roll in range(4):
    b.right(90)

c=Turtle()
c.color('green')
c.shape('turtle')
c.penup()
c.goto(-160,50)
c.pendown()

for roll in range(4):
    c.right(90)

d=Turtle()
d.color('purple')
d.shape('turtle')
d.penup()
d.goto(-160,20)
d.pendown()

for roll in range(4):
    d.right(90)

e=Turtle()
e.color('orange')
e.shape('turtle')
e.penup()
e.goto(-160,-10)
e.pendown()

for roll in range(4):
    e.right(90)

for turn in range(100): #And the race begins
    a.forward(randint(1,5)) #As anyone can see, the maximum the turtle may move is 500 pixels
    b.forward(randint(1,5)) #And the minimum they may move is 100
    c.forward(randint(1,5)) #But in any case, we will have our winner
    d.forward(randint(1,5)) #Thanks to the random function
    e.forward(randint(1,5))

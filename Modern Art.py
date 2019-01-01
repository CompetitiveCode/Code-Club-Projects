#!/bin/python3

from turtle import * #To draw things we need to import this
from random import * #To use the random number function

speed(0) #To speed the drawing, you can either delete/comment this line, or set a speed between 1-10

def randomcolor(): #This function is to create random colours
    red=randint(0,255) #For each color in R G B
    blue=randint(0,255) #We find a random number
    green=randint(0,255) #Between the valid values of 1 to 255 (256 possible values)
    color(red,green,blue)

def randomplace(): #This function is to place the pointer to draw at a random place
    penup() #So that as the pointer moves from A to B, it does not leave a trail.
    x = randint(-100,100) #Depending on the viewport, the X value in (-X,X) can be changed.
    y = randint(-100,100)
    goto(x,y) #This makes the pointer to move to that place which is found above
    pendown() #So that we can start drawing the shape

def randomheading(): #This function is to position the pointer head towards a random angle.
    setheading(randint(1,360)) #Possible values are 1 to 360 degree.
    
def drawrectangle(): #This function is to draw a rectangle
    randomcolor() #To call the randomcolor() to get a random color
    randomplace() #To call the randomplace() to get a random place
    hideturtle() #To hide the pointer while drawing the next figure
    length=randint(10,100) #Specifies the length of the rectangle
    height=randint(10,100) #Specifies the height of the rectangle
    begin_fill() #This is a function to fill the thing being drawed soon.
    forward(length) #This is drawing one side of a triangle
    right(90) #Then turning 90 degree as internal angle of a triangle is 90 degree
    forward(height)
    right(90)
    forward(length)
    right(90)
    forward(height)
    right(90)
    end_fill() #This specifies that the drawing is complete and to fill that shape with color
    
def drawdot():
    randomcolor()
    randomplace()
    dot(randint(1,200)) #This function draws a dot with a radius anywhere between 1 and 200

def drawstar():
    randomcolor()
    randomplace()
    begin_fill()
    temp=randint(20,100) #To select the length of the wings of a star
    for side in range(5):
        left(144) #Angle required so that a perfect angled star can be made
        forward(temp)
    end_fill()

shape("turtle")

for i in range(20):
    randomcolor()
    randomplace()
    randomheading()
    stamp() #To draw that shape, here "turtle" in the viewport

clear()
setheading(0) #So that the other shapes are not drawn with any angle

for i in range(20):
    drawrectangle()

clear()
    
for i in range(20):
    drawdot()

clear()
    
for i in range(20):
    drawstar()

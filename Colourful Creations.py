#!/bin/python3

from turtle import * #To import all the required functions in turtle

screen = Screen() #To draw a screen
screen.setup(400,400) #This specifies the dimension of the screen

colours = { #This specifies the colour dictionary to ease up editing colours
    'screenbg': '#2A27EC',
    'text1': '#CB27EC',
    'text2': '#EC272A',
    'dot': '#27ECD1'
}

screen.bgcolor(colours['screenbg']) #This specifies the color of the screen

color(colours['dot']) #To specify the dot's colour
dot(400) #To draw a dot with radius as the number specified and center as 0,0
#You can also draw a circle with: circle(400)

penup() #So that it does not draw the path the turtle moves. Comment this line to see the difference
goto(0,50) #To go to that specified location to start writing
color(colours['text1']) #This specifies the colour in which the content is to be written
style=('Verdana', 40, 'bold') #This specifies the font specification. We can also use Arial, etc. And change the size as well.
write('HELLO', font=style, align='center') #This specifies what is to be written, the font style and allignment.
hideturtle() #This is to hide the turtle from showing where it is currently

goto(0,-50)
color(colours['text2'])
write('WORLD', font=style, align='center') #You can also specify different style for this.

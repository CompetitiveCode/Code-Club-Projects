#!/bin/python3

#This program is depended on the data received from a website. So make sure that link is still working.

import json #To read values from the json input receiving
import turtle #To draw dots, setting background, etc.
import urllib.request #To request data from a URL
import time #To convert UNIX Time to Human Readable Form

screen = turtle.Screen() #Created a screen object
screen.setup(720, 360) #To setup the screen dimensions
screen.setworldcoordinates(-180,-90,180,90) #To set world coordinates
screen.bgpic('map.jpg') #To set a background picture

url = 'http://api.open-notify.org/astros.json' #The url from where we receive json input
response = urllib.request.urlopen(url) #Store the response from there to 'response'
result = json.loads(response.read()) #Reads the response with the help of 'json.loads'

print('People in Space: ',result['number']) #To print a particular value in 'result' called 'number'

people = result['people'] #To store all the values of 'people' in 'result' to a variable 'people'
for p in people: #To parse through each data values in 'people'
    print(p['name'],'in',p['craft'])

screen.register_shape('iss.png') #To define a new shape which in this case is 'iss.png'
iss = turtle.Turtle() #To create a Turlte object
iss.shape('iss.png') #To define the shape of that turtle
iss.setheading(90) #To define the angle of that shape in screen
    
url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('Latitude: ',lat,'\nLongitude: ',lon)

iss.penup()
iss.goto(lon,lat)

#Space Center, Houston
lat = 29.5502
lon = -95.097

location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon,lat)
location.dot(5)
location.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json'
url = url + '?lat=' + str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())
over = result['response'][1]['risetime']

style = ('Arial', 6, 'bold')
location.write(time.ctime(over), font=style)
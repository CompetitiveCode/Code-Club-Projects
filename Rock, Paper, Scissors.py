#!/bin/python3

from random import randint

player=''

while(player!='r' and player!='p' and player!='s'):
    print('Choose One: Rock (r), Paper (p) or Scissor (s): ',end='')
    player = input()
    if(player!='r' and player!='p' and player!='s'):
        print('Please choose the correct option')

chosen=randint(1,3)

if(chosen==1):
    computer='r'
elif(chosen==2):
    computer='p'
else:
    computer='s'

if(player==computer):
    result='DRAW'
else:
    if(player=='r' and computer=='s'):
        result='Player Wins'
    elif(player=='r' and computer=='p'):
        result='Computer Wins'
    if(player=='p' and computer=='r'):
        result='Player Wins'
    elif(player=='p' and computer=='s'):
        result='Computer Wins'
    if(player=='s' and computer=='p'):
        result='Player Wins'
    elif(player=='s' and computer=='r'):
        result='Computer Wins'

if(player=='r'):
    player='0'
elif(player=='s'):
    player='>8'
else:
    player='___'

if(computer=='r'):
    computer='0'
elif(computer=='s'):
    computer='>8'
else:
    computer='___'
    
print('\n',player,'vs',computer,'\n\n',result)

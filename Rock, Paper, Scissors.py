#!/bin/python3

from random import randint

playagain='y' #By default, the program should run once, so initialised to y
while(playagain=='y' or playagain=='Y'): #To play the game again
    player='' #Initialising

    while(player!='0' and player!='>8' and player!='___'): #To prompt for the correct choice
        print('\nChoose One: Rock (r), Paper (p) or Scissor (s): ',end='') 
        player = input()
        if(player!='r' and player!='p' and player!='s'): #This while loop will continue to run until a correct option is not added.
            print('Please choose the correct option')
        else: #And once the right option is added, the characters are changed for convenience
            if(player=='r'): 
                player='0' #Rock
            elif(player=='p'):
                player='___' #Paper
            else:
                player='>8' #Scissor
                
    chosen=randint(1,3) #This is for randomising what computer might choose in between rock, paper and scissor

    if(chosen==1): #This is to initialise the computer with the options
        computer='0'
    elif(chosen==2):
        computer='___'
    else:
        computer='>8'

    if(player==computer): #If both of them have the same values, then it is a draw
        result='DRAW'
    else: #If both of them have different choices, then this finds who wins
        if(player=='0' and computer=='>8'):
            result='Player Wins'
        elif(player=='0' and computer=='___'):
            result='Computer Wins'
        if(player=='___' and computer=='0'):
            result='Player Wins'
        elif(player=='___' and computer=='>8'):
            result='Computer Wins'
        if(player=='>8' and computer=='___'):
            result='Player Wins'
        elif(player=='>8' and computer=='0'):
            result='Computer Wins'
    
    print('\n',player,'vs',computer,'\n\n',result, '\n') #To print the result

    playagain='Choice Unknown' #To clear the choice to play again
    while(playagain!='y' and playagain!='n' and playagain!='Y' and playagain!='Y'): #Prompt to ask, whether they want to play again
        print('Would you like to play again? Yes(y) or No(n): ', end='')
        playagain=input()

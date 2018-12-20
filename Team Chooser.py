#!/bin/python3

from random import choice

print('Note: Please create players.txt and team.txt to include the players and team names and store it in the same place as this file is stored to run the program. Else there will be an error to execure this program\n\n')

players=[]
file=open('players.txt','r')
players=file.read().splitlines()
print('Players: ',players)

teams=[]
file=open('teams.txt','r')
teams=file.read().splitlines()
print('\nTeams: ',teams)

teamnameA=choice(teams)
teams.remove(teamnameA)
teamnameB=choice(teams)
teams.remove(teamnameB)
teamnameC=choice(teams)
teams.remove(teamnameC)

teamA=[]
teamB=[]
teamC=[]

while len(players) > 0:
    playerA=choice(players)
    teamA.append(playerA)
    players.remove(playerA)
    
    if players==[]:
        break

    playerB=choice(players)
    teamB.append(playerB)
    players.remove(playerB)

    if players==[]:
        break

    playerC=choice(players)
    teamC.append(playerC)
    players.remove(playerC)    

print('\nTeam ',teamnameA,': ', teamA,'\n\nTeam ',teamnameB,': ',teamB,'\n\nTeam ',teamnameC,': ',teamC)

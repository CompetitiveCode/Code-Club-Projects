#!/bin/python3

from random import choice #For random selection from a list

print('Note: Please create players.txt and team.txt to include the players and team names and store it in the same place as this file is stored to run the program. Else there will be an error to execure this program\n\n')

players=[] #To store the names of the players
file=open('players.txt','r') #The file players.txt will contain the names of the players
players=file.read().splitlines() #This will read each line of the text and store it as individual names in the list
print('Players: ',players) #To print the names of the players from the list

teams=[] #To store the names of the teams
file=open('teams.txt','r') #The file teams.txt will contain the names of the teams
teams=file.read().splitlines() #This will read each line of the text and store it as individual team in the list
print('\nTeams: ',teams) #To print the names of the teams from the list

teamnameA=choice(teams) #To select a team name from the list
teams.remove(teamnameA) #To remove that name from the list so that it is not reused
teamnameB=choice(teams)
teams.remove(teamnameB)
teamnameC=choice(teams)
teams.remove(teamnameC)

teamA=[] #To store names of players in each team
teamB=[]
teamC=[]

while len(players) > 0: #To run until there is no names left in the players list
    playerA=choice(players) #To select a name from the players list
    teamA.append(playerA) #To add that selected name to the team A list
    players.remove(playerA) #To remove the name of that player so that is it not selected by any other team
    
    if players==[]: #To get out of this loop if the players list becomes empty
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

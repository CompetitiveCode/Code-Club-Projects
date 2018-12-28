#!/bin/python3

alphabet = 'abcdefghijklmnopqrstuvwxyz' #Defines the characters which will be allowed
newMessage='' #To store the new message

message=input('Please Enter the Message (All Small Letters): ') #The message should be in small letters, else it won't be encrypted
key=int(input('Please Enter a Key (1-26): ')) #This is caesar cypher

for character in message: #Loops until there are characters in the message
    if character in alphabet: #Checks if the character is in alphabets or not
        position=alphabet.find(character) #To find the location of the character in alphabets
        newPosition=(position+key)%26 #To add the key and modulus is to go back to 0 after 25. 0 - 25 is 26 characters
        newCharacter=alphabet[newPosition] #To store the new encrypted alphabet into newCharacter
        newMessage+=newCharacter #To store the newCharacter with the entire encrypted message
    else: #If the character is not in alphabets (Capital Letters, Numbers, Special Symbols, etc)
        newMessage+=character

print(newMessage) #Prints the result
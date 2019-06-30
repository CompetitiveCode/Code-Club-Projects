#!/bin/python3

import random #To use the random choice function

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+[]{}\|;:<>,./?`~'
#Add any type of character you want your passwords to have
times = int(input('Enter the No. of passwords required: ')) #This stores the number of passwords required
for a in range(times):
    password = '' #Password is empty as it begins
    print('Enter the required length of password ',a+1,': ',end='') #The length of the password required
    length = int(input()) #You can also ask this length outside the for loop is you want same length passwords multiple times
    for c in range(length):
        password += random.choice(chars) # random.choice() to select random characters from 'chars' variable
    print(password)
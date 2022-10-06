#!/usr/bin/python3
from random import randrange


number = randrange(0,9999)
print(number)
userIn = str()


while len(userIn) != 4:
    userIn = input("Pick a 4 digit number: ")

while int(userIn) != number:
    print("Wrong guess! ", end='')
    userIn = input("Pick aother 4 didgit number: ")
print("You've got the right number! ")

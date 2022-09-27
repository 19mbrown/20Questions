#!/usr/bin/python3
import os.path

listOfNums = list()
inputNums = str()
yesOrNo = str()

while yesOrNo != "y":
    inputNums = input("Enter a number: ")
    listOfNums += inputNums
    yesOrNo = inputNums("Do you want to quit? (y/n) ")

print(max(listOfNums))
#!/usr/bin/python3
shoppingList = dict()

while True:
    item = input("What do you want to add? ")
    price = input("How much is it? (£) ")
    priority = input("How important is it? (1-20) ")
    shoppingList[item] = [price, priority]
    print(shoppingList[i])
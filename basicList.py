import os

yesOrNo = str()
listOfNames = list()

while yesOrNo != "y":
    name = input("Enter a name: ")
    listOfNames.append(name)
    yesOrNo = input("Do you want to carry on? (y/n) ")

listOfNames = listOfNames.lower()

printList = input("Do you want to print the list of names normally or reversed? (n/r) ")

if printList == "r":
    print(", ".join((listOfNames)).reverse())
elif printList == "n":
    print(listOfNames)

if input("Do you want to print out a specific number? (y/n) ") == "y":
    print(listOfNames[int(input(f"Which number do you want to print out? {len(listOfNames)} ") ) + 1])

if input("Do you want to print out the list sliced? (y/n) ") == "y":
    sliceStart = int(input("Where do you want to start at? ") + 1)
    sliceEnd = int(input("Where do you want to end at? ") + 1)
    print(listOfNames[sliceStart:sliceEnd])

if input("Do you want to remove any items? (y/n) ") == "y":
    listOfNames.remove(input("What item do you want to remove?"))

if input("Do you want to save this to a file? ") =="y":
    with open('bak.bak', 'w') as f:
        f.write(listOfNames)

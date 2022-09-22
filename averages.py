import statistics as s

yesOrNo = str()
listN = list()


while (yesOrNo != "y"):
    listN.append(int(input("Input a number: ")))
    yesOrNo = input("Do you want to quit? ")

print(f"The mean is: {s.mean(listN)} ")
print(f"The mode is: {s.mode(listN)} ")

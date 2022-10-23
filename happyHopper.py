list1 = input("Enter a number: ")
dif = []

for i in range(1, len(list1)):
    dif.append(int(list1[i]) - int(list1[i-1]))

for i in range(1, len(list1) - 1):
    if not (i in dif or (0-i) in dif):
        print("Not a Happy Hopper")
        exit(0)
print("Is a Happy Hopper")

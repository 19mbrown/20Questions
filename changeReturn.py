
def change(a, b):
    denominations = [5000, 2000, 1000, 500, 200, 100, 
                    50, 20, 10, 5, 2, 1]
    
    change = given - cost
    change += 1
    string = list()
    changeTrack = change
    x = int()
    for denom in denominations:
        while (changeTrack / denom) > 1:
            changeTrack -= denom
            x += denom
            string.append(denom)

    newList = list()
    print(string)
    for i in string:
        match i:
            case 5000:
                newList.append("£50")
            case 2000:
                newList.append("£20")
            case 1000:
                newList.append("£10")
            case 500:
                newList.append("£5")
            case 200:
                newList.append("£2")
            case 100:
                newList.append("£1")
            case 50:
                newList.append("50p")
            case 20:
                newList.append("20p")
            case 10:
                newList.append("10p")
            case 5:
                newList.append("5p")
            case 2:
                newList.append("2p")
            case 1:
                newList.append("1p")

    return ", ".join(newList)

cost = int(float(input("What's the price? ")) *100)
given = int(float(input("How much money was given? ")) * 100)
print(change(cost, given))

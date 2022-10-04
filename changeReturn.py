def change(a, b):
    denominations = [5000, 2000, 1000, 500, 200, 100, 
                    50, 20, 10, 5, 2, 1]
    
    change = b-a+1
    string = list()
    for denom in denominations:
        while (change / denom) > 1:
            change -= denom
            string.append(denom)
    hmr = ["£50", "£20", "£10", "£5", "£2", "£1", 
           "50p", "20p", "10p", "5p", "2p", "1p"]
    newList = list()

    for i in string:
        newList.append(hmr[denominations.index(i)])
    return ", ".join(newList)

cost = int(float(input("What's the price? ")) *100)
given = int(float(input("How much money was given? ")) * 100)
print(change(cost, given))

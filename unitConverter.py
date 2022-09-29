import requests

def currency(start, end, value):
    URL = "https://cdn.moneyconvert.net/api/latest.json"
    resp = requests.get(url=URL)
    data = resp.json()["rates"]

    toUSD = float(value / data[start])
    toEND = toUSD * data[end]
    return "{:.2f}".format(toEND)

def temp():
    start = input("What type of temp is it (c/f)? ")
    temp = float(input("What's the temp? "))
    if start == "c":
        return str((temp * (9/5)) + 32) + " F"
    elif start == "f":
        return str((temp - 32) * (5/9)) + " C"

def mass():
    start = input("Do you want to start at kilogram (k) or pounts (l)")
    value = float(input("What's the weight? "))
    if start == "k":
        return value * 2.20462
    elif start == "l":
        return value * 0.453592

whichConvert = input("What do you want to convert? \nCurrency (c), temp (t), mass (m)\n")

if whichConvert == "c":
    start = input("What's your starting currency? (ISO CODE) ").upper()
    end = input("What do you want to convert it to? (ISO CODE) ").upper()
    value = float(input("How much money? "))
    print(currency(start, end, value))
elif whichConvert == "t":
    print(temp())
elif whichConvert == "m":
    print(mass())

else:
    print("Not a valid input!!! ")
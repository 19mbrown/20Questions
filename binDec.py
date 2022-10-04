def decToBin(intInput):
    if intInput > 255:
        return "Number must be >= 255"
    else:
        binN = str("{0:b}".format(intInput))
        length = len(binN)
        binN = list(binN)
        for i in range(0, 8 - length):
            binN.insert(0, "0")
        binN = "".join(binN)
        return binN

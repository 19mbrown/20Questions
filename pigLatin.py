def pigLatin(word):
    pig = list(word)
    for i in f"{pig[0]}ay":
        pig.append(i)
    pig = "".join(pig[1:])
    return pig

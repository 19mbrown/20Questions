#!/usr/bin/python3
def countVowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    numberOfVowels = dict()
    for i in vowels:
        numberOfVowels[i] = string.lower().count(i)
    numberOfVowels["TOTAL"] = sum(numberOfVowels.values())
    return numberOfVowels

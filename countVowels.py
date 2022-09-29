def countVowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    numberOfVowels = dict()
    for i in vowels:
        numberOfVowels[i] = string.count(i)
    return numberOfVowels, sum(numberOfVowels.values())

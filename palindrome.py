#!/usr/bin/python3
def palindrome(word):
    wordList = list(word)
    wordBack = wordList[::-1]
    for i in range(len(wordList)):
        if wordBack[i] == wordList[i]:
            return True
        else:
            return False
            break

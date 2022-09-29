import string

def hangman(word):
    guessed = list()
    guesses = 7
    wrongGuessed = int()
    while wrongGuessed < guesses:
        letter = input("Enter a letter: ")
        if letter in word:
            print("Correct! ")
        else: 
            print("Wrong!")
            wrongGuessed+=1
        print(f"Lives: {guesses - wrongGuessed}")
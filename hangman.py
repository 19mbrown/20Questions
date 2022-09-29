#!/usr/bin/python3
def hangman(word):
    word = list(word.lower().strip())
    wordBak = list(word)
    guessed = list()
    guesses = 7
    guessedLetters = list()
    wrongGuessed = int()
    correctGuesses = list()

    while wrongGuessed < guesses:
        letter = input("Enter a letter: ").strip().lower()

        if letter in guessedLetters:
            print("Already guessed this letter")
        else:
            if letter in word:
                guessed.append(letter)
                print("Correct! ")
                wordBak.remove(letter)
            else:
                print("Wrong!")
                guessed.append(letter)
                wrongGuessed += 1
        print("───────────────────────────────")
        print(f"Lives: {guesses - wrongGuessed}")
        correctGuessesBak = correctGuesses
        for _ in range(word.count(letter)):
            correctGuesses.append(letter)

        print("Guessed:", ", ".join(guessed))
        print(correctGuesses)
        print("".join(correctGuesses))

        def new():
            for i in word:
                if i in correctGuessesBak:
                    x = True
                else:
                    x = False
                    break
            return x
        new()
        if new():
            print(f"Congrats! You've guessed the word! {word}")
            break

hangman("Hello")

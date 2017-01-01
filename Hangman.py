'''
Created on Jul 6, 2016

@author: Sheldon Jatou
'''
# WELCOME TO HANGMAN
from random import randint


def Guess():
    # Creates a few variables, as well as some possible words to be guessed.
    tries = 5
    final = ""
    guessed = []
    words = ["University of Toronto", "Computer Science",
             "Coffee", "Star Wars", "Side Project"]

    # Randomly selects a word from the list, and capitalizes it so that
    # when a user guesses a word, their choice of capitalization does not
    # matter.
    w = randint(0, len(words) - 1)
    selectedWord = words[w]

    selectedWord = selectedWord.upper()
    a = []

    # Makes 'a' an "empty" (underscores or spaces) list the length of the
    # selected word.
    for i in selectedWord:
        if i is not " ":
            a.append("_")
        elif i is " ":
            a.append(" ")

    print(
        "\nHello! Welcome to Hangman! Type a letter to guess, or type the word 'guess' to guess the phrase itself. \nWhile guessing, type 'back' to go back to only guessing letters. \nType 'quit' while guessing letters to exit the game.")

    # Displays the amount of tries the user has left, as well as the length of
    # the word they must guess ('a').
    while tries != 0:
        print("\nTries remaining: {}".format(tries))
        print(" ".join(a))

        g = input("Please guess a letter:")

        # If the user inputs a single letter that is in the selected word,
        # that letter is added to the list 'a' in its proper index location.
        if g.upper() in selectedWord and len(g) is 1 and g.upper() not in guessed:
            print("\nCorrect!")
            for i in range(len(list(selectedWord))):
                if list(selectedWord)[i] == g.upper():
                    a[i] = g.upper()

        # If the uses inputs the word 'guess', it allows them to guess the word
        # itself. If they guess correctly, they win! If not, they lose a try.
        # The user may also type 'quit' if they no longer wish the guess the
        # phrase. It also ensures that the user cannot guess numbers, and that
        # if they guess the same word more than once, they won't lose tries
        # for it.
        elif g.upper() == "GUESS":
            print("Type 'back' to go back.")

            final = input("Guess the phrase?:")

            if final.upper() == selectedWord:
                a = list(selectedWord)

            elif final.upper() == "BACK":
                print("Returning...")

            else:
                for i in final:
                    if not i.isalpha():
                        final = "N/A"
                if final == "N/A":
                    print(
                        "\nMake sure there are no numbers or special characters in your guess.")
                else:
                    print("\nInocrrect, sorry!")
                    if final.upper() not in guessed:
                        tries = tries - 1
                    elif final.upper() in guessed:
                        print(
                            "You already guessed that, try something else.")

        # Allows the user to exit the game by typing "quit".
        elif g.upper() == "QUIT":
            while True:
                l = input("Quit the game?(y or n): ")
                if l.upper() == 'Y':
                    return
                elif l.upper() == 'N':
                    break
                else:
                    print("Only 'y' or 'n', please.")

        # If the user inputs something that is has more than 1 character,
        # remind them they're doing it wrong.
        elif len(g) != 1:
            print("\nOnly guess letters, please.")

        # If the user guesses a number, don't take a try, but tell them to only put letters.
        # If the user simply guesses a letter not in the word, they lose a try.
        # They wont loose anything if they already guessed an incorrect letter.
        else:
            if not g.isalpha():
                print("\nOnly guess letters, please.")
            else:
                if g.upper() not in guessed:
                    print("\nWrong, try again.")
                    tries = tries - 1

        # When you guess a letter, so long as it is not 'guess'
        # it is added to a list so that you will not lose points for
        # guessing it twice.
        if g.upper() not in guessed and g.upper() != "GUESS":
            guessed.append(g.upper())

        elif g.upper() in guessed:
            print("\nAlready guessed that, try a different letter please.")

        # If the user guesses all letters correctly, they win (hooray!), and
        # are offered the chance to play again.
        # Also says different messages based on how many tries it took you.
        if a == list(selectedWord):
            print("".join(a))

            if tries == 5:
                print("You got it! Perfect!")
            elif tries == 4:
                print("You got it! Great job!")
            elif tries == 3:
                print("You got it! Good work.")
            elif tries == 2:
                print("You got it! Nice.")
            elif tries == 1:
                print("You got it! Close one.")

            while True:
                # Ensures that the user only selects 'y' or 'n'. If 'y', the
                # function restarts, and they get to play again. If 'n', the function
                # simply ends.
                p = input("Play again? (y or n):")
                if p.upper() == "Y":
                    Guess()
                    break
                elif p.upper() == "N":
                    break
                else:
                    print("'y' or 'n' only, please.")
            break

        # If they lose all their tries, they lose the game, and are offered to
        # play again (same as above)
        elif tries == 0:
            print("Game over!")
            while True:
                p = input("Play again? (y or n):")
                if p.upper() == "Y":
                    Guess()
                    break
                elif p.upper() == "N":
                    break
                else:
                    print("'y' or 'n' only, please.")
            break
Guess()

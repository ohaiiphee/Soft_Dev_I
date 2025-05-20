import random

def main():
    possibleWords = [
        "python",
        "monty",
        "parrot",
        "knights",
        "brian",
        "always",
        "look",
        "bright",
        "side",
        "life",
    ]
    scoresWord = []  # list of words to present on show score
    scoresCount = []  # list of amount of counts to show on score

    isGameStillGoing = True  # check if game is still ongoing
    while isGameStillGoing:
        # start navigation, if player chooses "e" game finishes, otherwise continue game
        checkForEndgame = navigation(possibleWords, scoresWord, scoresCount)
        if checkForEndgame == "e":
            print("Thanks for playing, goodbye!")
            isGameStillGoing = False  # escape while loop, stop game


def navigation(possibleWords, scoresWord, scoresCount):
    print("Welcome to Hangman! What would you like to do?")
    print("[n]ew game")
    print("[s]how score")
    print("[e]nd game")
    print("Your choice --> ", end="")

    choice = input().lower()

    match choice:
        case "n":
            print("Game starting...")
            start_game(possibleWords, scoresWord, scoresCount)
        case "s":
            print("Preparing scores...")
            show_scores(scoresWord, scoresCount)
        case "e":
            return "e"
        case _:
            # checked out https://blog.stackademic.com/python-match-case-statement-63d01477e1c0 to see how to use a default case
            # if input is not one of the valid choices, ask for input again and return to main to reprint nav
            print("")  # just some extra empty space to separate from previous nav
            print(
                "------------------------------------------------------------------------"
            )
            print(
                "Invalid input, please enter the letter [n], [s], or [e] (1 letter only!)"
            )
            print(
                "------------------------------------------------------------------------"
            )
            print("")  # just some extra empty space to separate from next nav
            return


def show_scores(scoresWord, scoresCount):
    if not scoresWord:
        print("")  # just some extra empty space to separate from previous nav
        print(
            "------------------------------------------------------------------------"
        )
        print(
            "You haven't played yet! Try guessing some words and come back to check your scores :)"
        )
        print(
            "------------------------------------------------------------------------"
        )
        print("")  # just some extra empty space to separate from next nav
    else:
        print("")
        print("These are your latest scores:")
        print("-------------------------------------------")
        for i in range(len(scoresWord)):
            print(f"The word '{scoresWord[i]}' was guessed in {scoresCount[i]} tries.")
        print("-------------------------------------------")
        print("")
    return  # leave show_scores, go back to main and reprint nav


def start_game(possibleWords, scoresWord, scoresCount):
    if not possibleWords:
        # when all words have been guessed, tell player that they have won the game
        print("")
        print(
            "---------------------------------------------------------------------------"
        )
        print(
            "You have guessed all the words and 100% completed the game, congratulations!"
        )
        print(
            "---------------------------------------------------------------------------"
        )
        print("")
        return  # when no more words are available to guess, simply return to navigation

    guessCounter = 0  # how many guesses so far
    lettersUsed = ""  # which chars have already been tried
    word = random.choice(possibleWords)  # get a word from the list above
    # remove this word from possibleWords so that it cannot be used again in future games in this session
    possibleWords.remove(word)

    guessedLetters = ""  # letters already guessed

    # print 1 underscore + space for every letter in word --> starts as all underscores bc no letter has been guessed yet
    for letter in word:
        guessedLetters += "_ "
    print(guessedLetters)

    get_letter(
        guessCounter,
        lettersUsed,
        guessedLetters,
        word,
        possibleWords,
        scoresWord,
        scoresCount,
    )


def get_letter(
    guessCounter,
    lettersUsed,
    guessedLetters,
    word,
    possibleWords,
    scoresWord,
    scoresCount,
):
    print("Please provide a letter: ", end="")
    letter = input()
    if len(letter) != 1 or letter.isnumeric():
        print("Only 1 letter (a-z) per try!")
        return get_letter(
            guessCounter,
            lettersUsed,
            guessedLetters,
            word,
            possibleWords,
            scoresWord,
            scoresCount,
        )
    letter = letter.lower()
    guessCounter += 1  # add to counter with every guess

    # check if letter has already been tried
    if letter in lettersUsed:
        # if yes, warn user and ask for new letter
        print("You've already tried that one!")
        print(guessedLetters)
        return get_letter(
            guessCounter,
            lettersUsed,
            guessedLetters,
            word,
            possibleWords,
            scoresWord,
            scoresCount,
        )
    else:
        # if not used yet, add to lettersUsed and continue
        lettersUsed += letter
        # check if letter is actually in the word to guess
        if letter in word:
            # new list to help switch empty guessedLetters with an updated version of guessedLetters
            updatedGuessedLetters = []
            for letter in word:
                if letter in lettersUsed:
                    updatedGuessedLetters.append(letter)
                else:
                    updatedGuessedLetters.append("_")
            # switch string of underscores (_ _ _ _) with string of underscores with lettersUsed (_ i _ e)
            guessedLetters = " ".join(updatedGuessedLetters)
            print(guessedLetters)  # print new state of guessedLetters
        else:
            print(f"Nope this word does not include {letter} - try again!")
            print(guessedLetters)
    # check if entire word has been guessed
    if "_" not in guessedLetters:
        # remove spaces in between letters to look nicer
        guessedLetters = "".join(guessedLetters.split())
        # update word and count scores
        scoresWord.append(word)
        scoresCount.append(guessCounter)
        print("")  
        print("--------------------------------------------------------------")
        print(
            f"Congratulations! You solved the word '{guessedLetters}' in {guessCounter} tries :)"
        )
        print("--------------------------------------------------------------")
        print("") 
        return  # leave get_letter when word has been fully guessed
    else:
        # continue with tries
        get_letter(
            guessCounter,
            lettersUsed,
            guessedLetters,
            word,
            possibleWords,
            scoresWord,
            scoresCount,
        )


main()

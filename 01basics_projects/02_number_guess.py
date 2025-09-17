from random import *

print("Welcome to Number Guessing Game!")
score = {"plays": 0, "losses": 0, "wins": 0}
done = False


def numberGuessing():
    guessesLeft = 5
    score["plays"] == 0 and print(
        "I will pick a random number and you will have to guess it"
    )
    randomInt = randint(0, 20)
    print(randomInt)
    userInt = int(input("Guess the number: "))

    while userInt != randomInt and guessesLeft != 0:
        guessesLeft -= 1
        message = f"Try again you have {guessesLeft} guesses left"

        if userInt > randomInt:
            print("Too High")
        else:
            print("Too Low")

        print(message)
        userInt = int(input("Guess the number: "))
    else:
        if randomInt == userInt:
            score["wins"] += 1
            print("Congratulations you made the right guess")
        else:
            score["losses"] += 1
            print(f"the random number is {randomInt}")


while not done:
    score["plays"] += 1
    numberGuessing()
    done = True if str(input("Do you want to restart? ")).lower() == "no" else False
else:
    print(f"Thanks for playing, you played {score['plays']} times, won {score['wins']} times and loss {score['losses']}")

"""⭐ Optional Improvements

Prevent the user from typing something that’s not a number (wrap int(input(...)) inside try/except).

Track wins and losses, not just plays.

Let the user pick the range (e.g. “Guess between 1 and 50”)."""

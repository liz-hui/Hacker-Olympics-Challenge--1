import random

print("HEY YOU. Want to win a free bubble tea? 🙂 \n")
print(
    "This program generates a random number from the user's range.\nPlease try your best to guess the correct number and win! \n")

# asks user for the range
min = input("What is the minimum number? \n")

# ensures it is a digit
if min.isdigit():
    min = int(min)
while type(min) is not int:
    min = input("Error. Only digits are allowed. What is the minimum number? \n")
    if min.isdigit():
        min = int(min)
        break

max = input("What is the maximum number? \n")

# ensures it is a digit
if max.isdigit():
    max = int(max)
while type(max) is not int:
    max = input("Error. Only digits are allowed. What is the maximum number? \n")
    if max.isdigit():
        max = int(max)
        break

# states the range
# print ("guess the number between the range" + min + " and " +max)

# Generates random number within a given range in Python
generated = random.randrange(min, max)

# guess = None

guess = input("\nWhat is your guess? \n")

# prompts user to guess random number
if guess.isdigit():
    guess = int(guess)

# tests if it is out of bounds
if guess > max or guess < min:
    print("You are out of bounds. \n Guess the number between the range " + str(min) + " and " + str(max))
    guess = input("\nWhat is your guess? \n")
    guess = int(guess)

# tests if it is an integer
while type(guess) is not int:
    guess = input("Error. Only integers are allowed. \n")
    guess = input("What is your guess? \n")

# comparison between guessed number and generated number
while type(guess) is int:
    guess = int(guess)

    if (generated > guess):
        print("BZZ WRONG")
        print("Incorrect. The number is higher.")
        guess = input("Guess again \n")
        guess = int(guess)

    if (generated < guess):
        print("BZZ WRONG")
        print("Incorrect. The number is lower.")
        guess = input("Guess again \n")
        guess = int(guess)

    if guess == generated:
        guess == int(guess)
        print("Congratulations! You guessed the number!")
        print("Contact SheHacks for your free bubble tea:)")
        break


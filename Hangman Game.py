import random

fruits = '''apple mango strawberry pineapple banana grapes watermelon papaya kiwi peach 
pear plum cherry lemon blueberry apricot pomegranate coconut lychee guava avocado grapefruit
tangerine raspberry blackberry cantaloupe durian passionfruit tamarind mangosteen custard 
starfruit longan rambutan dragonfruit lime kumquat jackfruit nectarine'''

SomeWords = fruits.split()
word = random.choice(SomeWords)

name = input("Enter your name: ")
print(f"Hello {name}, welcome to Hangman Game!")

attempts = 6
guessedLetters = set()

while attempts > 0:
    # show current progress
    for char in word:
        if char in guessedLetters:
            print(char, end=" ")
        else:
            print("_", end=" ")
    print()

    # check win
    if all(char in guessedLetters for char in word):
        print("Congratulations! You guessed the word:", word)
        break

    guessChar = input("Enter a letter: ").lower()

    if not guessChar.isalpha() or len(guessChar) != 1:
        print("Please enter a single alphabetic character.")
        continue
    if guessChar in guessedLetters:
        print("You already guessed that letter.")
        continue

    guessedLetters.add(guessChar)

    if guessChar not in word:
        attempts -= 1
        print(f"Wrong guess! Attempts left: {attempts}")

else:
    print("You lost! The word was:", word)

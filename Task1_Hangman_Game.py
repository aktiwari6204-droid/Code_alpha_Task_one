"""
CodeAlpha - Python Programming Task 1
Project: Hangman Game

Description:
A simple console-based Hangman game using a predefined list of words.
The player gets a maximum of 6 incorrect guesses.
"""

import random

WORDS = ["python", "developer", "computer", "programming", "analytics"]
MAX_INCORRECT_GUESSES = 6


def play_hangman():
    word = random.choice(WORDS)
    guessed_letters = set()
    incorrect_guesses = 0

    print("=" * 45)
    print("          HANGMAN GAME - CODEALPHA")
    print("=" * 45)
    print("Guess the word one letter at a time.")
    print(f"You have {MAX_INCORRECT_GUESSES} incorrect guesses.\n")

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        display_word = " ".join(
            letter if letter in guessed_letters else "_" for letter in word
        )

        print("Word:", display_word)
        print("Guessed letters:", " ".join(sorted(guessed_letters)) or "None")
        print(
            f"Incorrect guesses: {incorrect_guesses}/{MAX_INCORRECT_GUESSES}"
        )

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            return

        guess = input("Enter a single letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabetic letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct guess!\n")
        else:
            incorrect_guesses += 1
            print("Incorrect guess!\n")

    print("Game Over!")
    print("The correct word was:", word)


if __name__ == "__main__":
    play_hangman()

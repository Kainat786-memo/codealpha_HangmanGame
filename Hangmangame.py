import random

# List of predefined words
words = ["python", "apple", "school", "computer", "banana"]

# Randomly choose a word
secret_word = random.choice(words)

# Create hidden word
guessed_word = ["_"] * len(secret_word)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
attempts = 6

print("=" * 40)
print("       WELCOME TO HANGMAN GAME")
print("=" * 40)

while attempts > 0 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Incorrect guesses left:", attempts)
    print("Guessed letters:", ", ".join(guessed_letters))

    guess = input("Enter a letter: ").lower()

    # Check input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct!")

        # Reveal all matching letters
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong guess!")
        attempts -= 1

# Final result
print("\n" + "=" * 40)

if "_" not in guessed_word:
    print("Congratulations! You guessed the word.")
    print("The word was:", secret_word)
else:
    print("Game Over!")
    print("The correct word was:", secret_word)

print("=" * 40)
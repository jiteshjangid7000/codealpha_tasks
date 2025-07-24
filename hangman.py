import random

word_list = ["apple", "tiger", "chair", "house", "train"]


word_to_guess = random.choice(word_list)

guessed_letters = []

max_attempts = 6
attempts_left = max_attempts

def display_word():
    display = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


print("Welcome to Hangman!")
while attempts_left > 0:
    print("\nWord to guess:", display_word())
    print("Guessed letters:", " ".join(guessed_letters))
    print("Attempts left:", attempts_left)

    guess = input("Guess a letter: ").lower()

   
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("Good guess!")
    else:
        print("Wrong guess!")
        attempts_left -= 1

    if all(letter in guessed_letters for letter in word_to_guess):
        print("\nCongratulations! You guessed the word:", word_to_guess)
        break
else:
    print("\nGame Over! The word was:", word_to_guess)

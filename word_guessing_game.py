import random

def choose_word():
    # List of six-letter words
    words = ["banana", "cherry", "orange", "grapes", "tomato", "carrot", "pepper", "celery"]
    # Randomly select a word from the list
    return random.choice(words)

def get_guess():
    # Get a guess from the player
    guess = input("Enter your guess (six-letter word): ").lower()
    while len(guess) != 6:
        print("Invalid input. Please enter a six-letter word.")
        guess = input("Enter your guess (six-letter word): ").lower()
    return guess

def give_feedback(guess, word):
    # Provide feedback on the guess
    feedback = ["_"] * 6
    for i in range(6):
        if guess[i] == word[i]:
            feedback[i] = guess[i]
        elif guess[i] in word:
            feedback[i] = "*"
    return "".join(feedback)

def play_game():
    word = choose_word()
    attempts = 10
    print("Welcome to the Word Guessing Game!")
    print(f"You have {attempts} attempts to guess the six-letter word.")

    while attempts > 0:
        guess = get_guess()
        if guess == word:
            print(f"Congratulations! You guessed the word correctly: {word}")
            return
        else:
            feedback = give_feedback(guess, word)
            print(f"Feedback: {feedback}")
            attempts -= 1
            print(f"Attempts remaining: {attempts}")

    print(f"Sorry, you've run out of attempts. The word was: {word}")

if __name__ == "__main__":
    play_game()

import random

def get_valid_input():
    while True:
        user_input = input("Guess a number between 0 and 100: ")
        try:
            guess = int(user_input)
            if 0 <= guess <= 100:
                return guess
            else:
                print("Oops! Please enter a number between 0 and 100.")
        except ValueError:
            print("That's not a valid number! Please enter an integer between 0 and 100.")

def evaluate_guess(guess, secret_number):
    if guess < secret_number:
        return "low"
    elif guess > secret_number:
        return "high"
    else:
        return "correct"

def play_game():
    secret_number = random.randint(0, 100)
    print("\nWelcome to the Higher/Lower Guessing Game!")
    print("I'm thinking of a number between 0 and 100. Can you guess what it is?")

    while True:
        guess = get_valid_input()
        result = evaluate_guess(guess, secret_number)

        if result == "low":
            print("Too low! Try a higher number.\n")
        elif result == "high":
            print("Too high! Try a lower number.\n")
        else:
            print(f"Congratulations! You guessed it right. The number was {secret_number}.")
            break

if __name__ == "__main__":
    play_game()

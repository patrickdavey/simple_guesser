import random

def parse_guess(user_input: str):
  "not implemented"

def evaluate_guess(guess, secret_number):
  "not implemented"

def play_game():
    secret_number = random.randint(0, 100)
    print("\nWelcome to the Higher/Lower Guessing Game!")
    print("I'm thinking of a number between 0 and 100. Can you guess what it is?")

    while True:
        user_input = input("Guess a number between 0 and 100: ")
        status, guess = parse_guess(user_input)

        if status == "invalid":
            print("That's not a valid number! Please enter an integer between 0 and 100.")
        elif status == "out_of_range":
            print("Oops! Please enter a number between 0 and 100.")
        else:
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

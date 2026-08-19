import random


def get_valid_int(prompt):
    while True:
        value = input(prompt)
        if value.lstrip("-").isdigit():
            return int(value)
        print("Please enter a valid integer.")


def play_game(low=1, high=100, max_attempts=7):
    target = random.randint(low, high)
    attempts = 0

    print(f"Guess a number between {low} and {high}. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        guess = get_valid_int("Your guess: ")
        attempts += 1

        if guess == target:
            print(f"Correct! You guessed it in {attempts} attempt(s).")
            return
        elif guess < target:
            print("Too low.")
        else:
            print("Too high.")

    print(f"Out of attempts! The number was {target}.")


play_game()

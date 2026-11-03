import random

number = random.randint(1, 100)

score = 100
attempts = 0
max_attempts = 10

while attempts < max_attempts:

    guess = int(input("Guess a number between 1 and 100: "))

    attempts = attempts + 1

    if guess == number:
        print("Correct!")
        print("Final Score:", score)
        break

    else:
        score = score - 10

        if guess < number:
            print("Too low")
        else:
            print("Too high")

        if number % 2 == 0:
            print("Hint: Number is even")
        else:
            print("Hint: Number is odd")

        if number % 5 == 0:
            print("Hint: Number is multiple of 5")
        else:
            print("Hint: Number is not multiple of 5")

else:
    print("You lost!")
    print("The number was:", number)
    print("Score: 0")

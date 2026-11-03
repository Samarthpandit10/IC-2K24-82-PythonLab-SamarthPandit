low = int(input("Enter starting number: "))
high = int(input("Enter ending number: "))

print("Think of a number between", low, "and", high)

count = 0

while low <= high:

    guess = (low + high) // 2
    count = count + 1

    print("Computer guess:", guess)

    answer = input(
        "Enter H for too high, L for too low, C for correct: "
    )

    if answer == "C" or answer == "c":
        print("Computer guessed your number!")
        print("Guesses:", count)
        break

    elif answer == "H" or answer == "h":
        high = guess - 1

    elif answer == "L" or answer == "l":
        low = guess + 1

    else:
        print("Invalid input")

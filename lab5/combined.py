import random


def atm():

    balance = 5000
    pin = 1234

    user_pin = int(input("Enter PIN: "))

    if user_pin != pin:
        print("Wrong PIN")
        return

    while True:

        print("\n--- ATM ---")
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            print("Balance:", balance)

        elif choice == 2:
            amount = int(input("Enter amount: "))
            balance = balance + amount

        elif choice == 3:
            amount = int(input("Enter amount: "))

            if amount <= balance:
                balance = balance - amount
                print("Withdrawal successful")
            else:
                print("Insufficient balance")

        elif choice == 4:
            break


def grade_calculator():

    marks = []

    for i in range(5):
        mark = float(input("Enter marks: "))
        marks.append(mark)

    average = sum(marks) / 5

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    print("Average:", average)
    print("Grade:", grade)


def guessing_game():

    number = random.randint(1, 100)
    score = 100

    for i in range(10):

        guess = int(input("Guess the number: "))

        if guess == number:
            print("Correct!")
            print("Score:", score)
            return

        score = score - 10
        print("Wrong guess")

    print("You lost")
    print("Score: 0")


while True:

    print("\n===== MAIN MENU =====")
    print("1. ATM")
    print("2. Grade Calculator")
    print("3. Guessing Game")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        atm()

    elif choice == 2:
        grade_calculator()

    elif choice == 3:
        guessing_game()

    elif choice == 4:
        print("Thank you")
        break

    else:
        print("Invalid choice")

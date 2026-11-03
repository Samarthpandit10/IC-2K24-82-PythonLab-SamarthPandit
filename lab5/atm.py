balance = 5000
pin = 1234

user_pin = int(input("Enter PIN: "))

if user_pin == pin:
    while True:
        print("\n1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            print("Balance:", balance)

        elif choice == 2:
            amount = int(input("Enter amount: "))
            balance = balance + amount
            print("New balance:", balance)

        elif choice == 3:
            amount = int(input("Enter amount: "))

            if amount <= balance:
                balance = balance - amount
                print("Withdrawal successful")
            else:
                print("Insufficient balance")

        elif choice == 4:
            break

        else:
            print("Invalid choice")
else:
    print("Wrong PIN")

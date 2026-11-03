total = 0
average = 0
grade = ""

while True:
    print("\n1. Enter marks")
    print("2. View grade")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        total = 0

        for i in range(5):
            marks = int(input("Enter marks: "))
            total += marks

        average = total / 5

        if average >= 90:
            grade = "A"
        elif average >= 80:
            grade = "B"
        elif average >= 70:
            grade = "C"
        elif average >= 60:
            grade = "D"
        else:
            grade = "F"

    elif choice == 2:
        print("Average:", average)
        print("Grade:", grade)

    elif choice == 3:
        break

    else:
        print("Invalid choice")

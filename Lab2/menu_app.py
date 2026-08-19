import math


def get_valid_int(prompt, allow_negative=False):
    while True:
        value = input(prompt)
        check_value = value.lstrip("-") if allow_negative else value
        if check_value.isdigit():
            return int(value)
        print("Please enter a valid integer.")


# ---- Armstrong ----
def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    return sum(int(d) ** power for d in digits) == num


def run_armstrong():
    num = get_valid_int("Enter a number: ")
    print(f"{num} is {'an' if is_armstrong(num) else 'not an'} Armstrong number.")


# ---- Prime ----
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def run_prime():
    num = get_valid_int("Enter a number: ")
    print(f"{num} is {'' if is_prime(num) else 'not '}prime.")


# ---- Perfect ----
def is_perfect(num):
    if num < 1:
        return False
    return sum(i for i in range(1, num) if num % i == 0) == num


def run_perfect():
    num = get_valid_int("Enter a number: ")
    print(f"{num} is {'' if is_perfect(num) else 'not '}a perfect number.")


# ---- Palindrome ----
def is_palindrome_number(num):
    original = num
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    return original == reversed_num


def run_palindrome():
    num = get_valid_int("Enter a number: ")
    print(f"{num} is {'' if is_palindrome_number(num) else 'not '}a palindrome.")


# ---- Fibonacci ----
def fibonacci_loop(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


def run_fibonacci():
    n = get_valid_int("Enter number of terms: ")
    print("Fibonacci series:", fibonacci_loop(n))


# ---- Patterns ----
def run_patterns():
    n = get_valid_int("Enter number of rows: ")
    print("\nRight-angled triangle:")
    for i in range(1, n + 1):
        print("*" * i)

    print("\nNumber pattern:")
    for i in range(1, n + 1):
        print("".join(str(num) for num in range(1, i + 1)))

    print("\nPyramid pattern:")
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))


def show_menu():
    print("\n===== Menu =====")
    print("1. Check Armstrong number")
    print("2. Check prime number")
    print("3. Check perfect number")
    print("4. Check palindrome number")
    print("5. Print Fibonacci series")
    print("6. Print patterns")
    print("7. Exit")


def main():
    actions = {
        "1": run_armstrong,
        "2": run_prime,
        "3": run_perfect,
        "4": run_palindrome,
        "5": run_fibonacci,
        "6": run_patterns,
    }

    while True:
        show_menu()
        choice = input("Choose an option (1-7): ")

        if choice == "7":
            print("Exiting. Goodbye!")
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Invalid choice, please try again.")


main()

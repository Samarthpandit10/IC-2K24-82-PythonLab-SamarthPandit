# This program checks whether a number is an Armstrong number, and can
# also print all Armstrong numbers in a range given by the user.
# An Armstrong number equals the sum of its own digits each raised to
# the power of the number of digits (e.g. 153 = 1^3 + 5^3 + 3^3).


def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == num


def armstrong_in_range(start, end):
    return [n for n in range(start, end + 1) if is_armstrong(n)]


def get_valid_int(prompt):
    # Keep asking until the user gives a valid non-negative integer
    while True:
        value = input(prompt)
        if value.lstrip("-").isdigit() and int(value) >= 0:
            return int(value)
        print("Please enter a valid non-negative integer.")


num = get_valid_int("Enter a number: ")
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

start = get_valid_int("Enter range start: ")
end = get_valid_int("Enter range end: ")
result = armstrong_in_range(start, end)
print(f"Armstrong numbers between {start} and {end}: {result}")

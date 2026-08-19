
def is_perfect(num):
    if num < 1:
        return False
    divisor_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisor_sum == num and num != 0


def perfect_up_to(limit):
    return [n for n in range(1, limit + 1) if is_perfect(n)]


def get_valid_int(prompt):
    while True:
        value = input(prompt)
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("Please enter a valid positive integer.")


num = get_valid_int("Enter a number: ")
if is_perfect(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")

limit = get_valid_int("Enter a limit: ")
print(f"Perfect numbers up to {limit}: {perfect_up_to(limit)}")

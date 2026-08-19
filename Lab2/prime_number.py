import math


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def primes_up_to(limit):
    return [n for n in range(2, limit + 1) if is_prime(n)]


def get_valid_int(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        print("Please enter a valid non-negative integer.")


num = get_valid_int("Enter a number: ")
if is_prime(num):
    print(f"{num} is prime.")
else:
    print(f"{num} is not prime.")

limit = get_valid_int("Enter a limit: ")
print(f"Prime numbers up to {limit}: {primes_up_to(limit)}")

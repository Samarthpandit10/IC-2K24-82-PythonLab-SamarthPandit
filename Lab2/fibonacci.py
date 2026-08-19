call_count = 0


def fibonacci_loop(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


def fibonacci_recursive(n):
    global call_count
    call_count += 1
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def get_valid_int(prompt):
    while True:
        value = input(prompt)
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("Please enter a valid positive integer.")


n = get_valid_int("Enter number of terms: ")

print("Loop-based Fibonacci:", fibonacci_loop(n))

recursive_series = []
for i in range(n):
    recursive_series.append(fibonacci_recursive(i))
print("Recursive Fibonacci:", recursive_series)

print(f"Recursive version made {call_count} function calls for n = {n}.")

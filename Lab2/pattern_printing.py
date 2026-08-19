def print_star_triangle(n):
    for i in range(1, n + 1):
        print("*" * i)


def print_number_pattern(n):
    for i in range(1, n + 1):
        row = "".join(str(num) for num in range(1, i + 1))
        print(row)


def print_pyramid(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)


def get_valid_int(prompt):
    while True:
        value = input(prompt)
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("Please enter a valid positive integer.")


rows = get_valid_int("Enter number of rows: ")

print("\nRight-angled triangle:")
print_star_triangle(rows)

print("\nNumber pattern:")
print_number_pattern(rows)

print("\nPyramid pattern:")
print_pyramid(rows)

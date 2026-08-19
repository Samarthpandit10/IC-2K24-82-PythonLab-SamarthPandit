
def is_palindrome_number(num):
    original = num
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    return original == reversed_num


def is_palindrome_string(text):
    return text == text[::-1]


def get_valid_int(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        print("Please enter a valid non-negative integer.")


num = get_valid_int("Enter a number: ")
if is_palindrome_number(num):
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")

text = input("Enter a string: ")
if is_palindrome_string(text):
    print(f'"{text}" is a palindrome string.')
else:
    print(f'"{text}" is not a palindrome string.')

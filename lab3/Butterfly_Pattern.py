def print_butterfly(n):
    for i in range(1, n + 1):
        stars = i
        spaces_middle = 2 * (n - i)

        left = "*" * stars
        right = "*" * stars
        if spaces_middle > 0:
            print(left + " " * spaces_middle + right)
        else:
            print(left + right)  

    for i in range(n - 1, 0, -1):
        stars = i
        spaces_middle = 2 * (n - i)

        left = "*" * stars
        right = "*" * stars
        if spaces_middle > 0:
            print(left + " " * spaces_middle + right)
        else:
            print(left + right)

print_butterfly(5)
print()
print_butterfly(4)

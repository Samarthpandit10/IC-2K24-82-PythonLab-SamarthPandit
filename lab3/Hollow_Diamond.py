def print_hollow_diamond(n):
    if n % 2 == 0:
        print("n must be odd")
        return

    mid = n // 2
  
    for i in range(mid + 1):
        spaces_before = mid - i
        gap_between = 2 * i - 1  

        row = " " * spaces_before + "*"
        if gap_between > 0:
            row += " " * gap_between + "*"
        print(row)

    for i in range(mid - 1, -1, -1):
        spaces_before = mid - i
        gap_between = 2 * i - 1

        row = " " * spaces_before + "*"
        if gap_between > 0:
            row += " " * gap_between + "*"
        print(row)

print_hollow_diamond(7)
print()
print_hollow_diamond(5)

matrix = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# Input
for i in range(3):
    for j in range(3):
        matrix[i][j] = int(input("Enter: "))

# Display matrix
print("\nMatrix:")
for i in range(3):
    for j in range(3):
        print(matrix[i][j], end=" ")
    print()

# Sum of all elements
total = 0

for i in range(3):
    for j in range(3):
        total = total + matrix[i][j]

print("Sum of all elements:", total)

# Sum of main diagonal
diagonal = 0

for i in range(3):
    diagonal = diagonal + matrix[i][i]

print("Sum of main diagonal:", diagonal)

# Largest element
largest = matrix[0][0]

for i in range(3):
    for j in range(3):
        if matrix[i][j] > largest:
            largest = matrix[i][j]

print("Largest element:", largest)

# Smallest element
smallest = matrix[0][0]

for i in range(3):
    for j in range(3):
        if matrix[i][j] < smallest:
            smallest = matrix[i][j]

print("Smallest element:", smallest)

# Transpose
print("\nTranspose:")
for i in range(3):
    for j in range(3):
        print(matrix[j][i], end=" ")
    print()

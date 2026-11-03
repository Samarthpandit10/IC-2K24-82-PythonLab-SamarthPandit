# Time and Space Complexity Activity

## Introduction

This activity contains 22 Python code snippets. For each snippet, the time complexity and space complexity are given with a simple explanation.

### Big-O Notation Used

- `O(1)` → Constant
- `O(log n)` → Logarithmic
- `O(n)` → Linear
- `O(n log n)` → Linearithmic
- `O(n²)` → Quadratic
- `O(n³)` → Cubic
- `O(2ⁿ)` → Exponential

---

## Snippet 1 - Find Maximum

### Code

```python
def find_max(arr):
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val
```

### Answer

**Time Complexity:** `O(n)`

**Time Reason:** The loop checks every element once, so for `n` elements it performs `n` operations.

**Space Complexity:** `O(1)`

**Space Reason:** Only `max_val` and the loop variable are used as extra variables; no extra memory grows with `n`.

---

## Snippet 2 - Check Duplicate

### Code

```python
def has_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False
```

### Answer

**Time Complexity:** `O(n²)`

**Time Reason:** There are two nested loops, so elements can be compared approximately `n × n` times.

**Space Complexity:** `O(1)`

**Space Reason:** Only `i` and `j` are used as extra variables, so additional memory remains constant.

---

## Snippet 3 - Sum of Digits

### Code

```python
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)
```

### Answer

**Time Complexity:** `O(log n)`

**Time Reason:** Each recursive call divides `n` by 10, so the number of calls is logarithmic.

**Space Complexity:** `O(log n)`

**Space Reason:** Each recursive call remains on the call stack until the function finishes.

---

## Snippet 4 - Print Pairs

### Code

```python
def print_pairs(arr):
    n = len(arr)
    result = []
    for i in range(n):
        for j in range(n):
            result.append((arr[i], arr[j]))
    return result
```

### Answer

**Time Complexity:** `O(n²)`

**Time Reason:** The two nested loops each run `n` times, producing `n²` pairs.

**Space Complexity:** `O(n²)`

**Space Reason:** The `result` list stores all `n²` generated pairs.

---

## Snippet 5 - Binary Search

### Code

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

### Answer

**Time Complexity:** `O(log n)`

**Time Reason:** Binary search removes approximately half of the remaining elements during every iteration.

**Space Complexity:** `O(1)`

**Space Reason:** Only `low`, `high`, and `mid` are stored, so extra memory remains constant.

---

## Snippet 6 - Matrix Multiplication

### Code

```python
def matrix_multiply(a, b):
    n = len(a)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
    return result
```

### Answer

**Time Complexity:** `O(n³)`

**Time Reason:** There are three nested loops, each running `n` times, giving `n × n × n = n³`.

**Space Complexity:** `O(n²)`

**Space Reason:** The `result` matrix contains `n × n` elements.

---

## Snippet 7 - Convert to Sparse Matrix

### Code

```python
def to_sparse(matrix):
    triples = []
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] != 0:
                triples.append((r, c, matrix[r][c]))
    return triples
```

### Answer

**Time Complexity:** `O(mn)`

**Time Reason:** The nested loops visit every cell of the `m × n` matrix exactly once.

**Space Complexity:** `O(k)`

**Space Reason:** `triples` stores only the `k` non-zero elements of the matrix.

---

## Snippet 8 - Process Array

### Code

```python
def process(arr):
    n = len(arr)
    for i in range(n):
        print(arr[i])
    for j in range(n):
        for k in range(n):
            print(arr[j], arr[k])
```

### Answer

**Time Complexity:** `O(n²)`

**Time Reason:** The first loop takes `O(n)` and the nested loops take `O(n²)`; the larger term dominates.

**Space Complexity:** `O(1)`

**Space Reason:** Only loop variables and `n` are used; no extra data structure grows with `n`.

---

## Snippet 9 - Check First Ten

### Code

```python
def check_first_ten(arr):
    for i in range(len(arr)):
        for j in range(10):
            if arr[i] == j:
                return True
    return False
```

### Answer

**Time Complexity:** `O(n)`

**Time Reason:** The outer loop runs `n` times and the inner loop always runs only 10 times, so `10n` simplifies to `O(n)`.

**Space Complexity:** `O(1)`

**Space Reason:** Only loop variables are used and no additional memory grows with the input.

---

## Snippet 10 - Reverse Using New List

### Code

```python
def reverse_new(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr
```

### Answer

**Time Complexity:** `O(n)`

**Time Reason:** The loop visits every element once and adds each element to the new list.

**Space Complexity:** `O(n)`

**Space Reason:** `reversed_arr` stores all `n` elements of the input.

---

## Snippet 11 - Reverse In Place

### Code

```python
def reverse_in_place(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
```

### Answer

**Time Complexity:** `O(n)`

**Time Reason:** The loop performs approximately `n/2` swaps, which is still `O(n)`.

**Space Complexity:** `O(1)`

**Space Reason:** The reversal is done in the original array using only `left` and `right`, so no extra list is created.

---

## Snippet 12 - Factorial

### Code

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
```

### Answer

**Time Complexity:** `O(n)`

**Time Reason:** The function recursively decreases `n` by 1 until it reaches 1, resulting in `n` calls.

**Space Complexity:** `O(n)`

**Space Reason:** The recursive calls remain on the call stack before the function returns.

---

## Snippet 13 - Fibonacci

### Code

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

### Answer

**Time Complexity:** `O(2ⁿ)`

**Time Reason:** Each call creates two more recursive calls, causing the number of calls to grow exponentially.

**Space Complexity:** `O(n)`

**Space Reason:** The maximum depth of the recursive call stack is `n`.

---

## Snippet 14 - Count Pairs With Sum

### Code

```python
def count_pairs_with_sum(arr, target):
    seen = set()
    count = 0
    for num in arr:
        if target - num in seen:
            count += 1
        seen.add(num)
    return count
```

### Answer

**Time Complexity:** `O(n)`

**Time Reason:** The loop goes through the array once, and set lookup and insertion are average `O(1)` operations.

**Space Complexity:** `O(n)`

**Space Reason:** The `seen` set can store up to `n` different elements.

---

## Snippet 15 - Print All Subsets

### Code

```python
def print_all_subsets(arr):
    n = len(arr)
    for i in range(2 ** n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(arr[j])
        print(subset)
```

### Answer

**Time Complexity:** `O(n × 2ⁿ)`

**Time Reason:** There are `2ⁿ` possible subsets, and for each subset the inner loop checks `n` elements.

**Space Complexity:** `O(n)`

**Space Reason:** The temporary `subset` list can contain up to `n` elements.

---

## Snippet 16 - Merge Sorted Arrays

### Code

```python
def merge_sorted(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
```

### Answer

Let `n = len(a)` and `m = len(b)`.

**Time Complexity:** `O(n + m)`

**Time Reason:** Every element from arrays `a` and `b` is processed at most once.

**Space Complexity:** `O(n + m)`

**Space Reason:** The `result` list stores all elements from both arrays.

---

## Snippet 17 - Check Palindrome

### Code

```python
def is_palindrome(s):
    return s == s[::-1]
```

### Answer

**Time Complexity:** `O(n)`

**Time Reason:** The string is processed to create the reversed copy and compare the strings.

**Space Complexity:** `O(n)`

**Space Reason:** `s[::-1]` creates a new reversed string containing `n` characters.

---

## Snippet 18 - Flatten Matrix

### Code

```python
def flatten(matrix):
    flat = []
    for row in matrix:
        for val in row:
            flat.append(val)
    return flat
```

### Answer

**Time Complexity:** `O(mn)`

**Time Reason:** The nested loops visit every element in the `m × n` matrix exactly once.

**Space Complexity:** `O(mn)`

**Space Reason:** The `flat` list stores all `m × n` elements.

---

## Snippet 19 - Power

### Code

```python
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)
```

### Answer

**Time Complexity:** `O(exp)`

**Time Reason:** The exponent decreases by 1 in every recursive call, resulting in `exp` calls.

**Space Complexity:** `O(exp)`

**Space Reason:** All recursive calls remain on the call stack until the base case is reached.

---

## Snippet 20 - Fast Power

### Code

```python
def fast_power(base, exp):
    if exp == 0:
        return 1
    half = fast_power(base, exp // 2)
    if exp % 2 == 0:
        return half * half
    return half * half * base
```

### Answer

**Time Complexity:** `O(log exp)`

**Time Reason:** The exponent is divided by 2 in every recursive call, so the number of calls is logarithmic.

**Space Complexity:** `O(log exp)`

**Space Reason:** There are `O(log exp)` recursive calls stored on the call stack.

---

## Snippet 21 - Common Element

### Code

```python
def has_common_element(a, b):
    for x in a:
        for y in b:
            if x == y:
                return True
    return False
```

### Answer

Let `n = len(a)` and `m = len(b)`.

**Time Complexity:** `O(nm)`

**Time Reason:** Each element of `a` may be compared with every element of `b`, giving `n × m` comparisons.

**Space Complexity:** `O(1)`

**Space Reason:** Only `x` and `y` are used as extra variables; no additional data structure is created.

---

## Snippet 22 - Build Frequency Map

### Code

```python
def build_frequency_map(arr):
    freq = {}
    for val in arr:
        freq[val] = freq.get(val, 0) + 1
    return freq
```

### Answer

**Time Complexity:** `O(n)`

**Time Reason:** The loop visits each element once, and dictionary operations are average `O(1)`.

**Space Complexity:** `O(n)`

**Space Reason:** The `freq` dictionary can contain up to `n` different values.

---


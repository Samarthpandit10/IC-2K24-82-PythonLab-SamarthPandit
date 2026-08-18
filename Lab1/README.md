Lab 1 — Python

## 1. variable_practice.py
**Aim:** Declare variables of different types and print each with its type.

**Logic:** Create four variables — name (str), age (int), height (float), and
is_student (bool). Print each variable next to the result of `type()` called
on it.

**Sample Input/Output:**
```
Samarth <class 'str'>
20 <class 'int'>
5.9 <class 'float'>
True <class 'bool'>
```

---

## 2. greeting.py
**Aim:** Take a user's name, age, and city, and greet them in one sentence.

**Logic:** Read three inputs with `input()`. Combine them into one sentence
using an f-string.

**Sample Input/Output:**
```
Enter your name: Samarth
Enter your age: 20
Enter your city: Indore
Hi, I'm Samarth, I'm 20 years old, and I live in Indore.
```

---

## 3. arithmetic.py
**Aim:** Take two numbers and print their sum, difference, product,
quotient, and remainder.

**Logic:** Read two inputs and convert them to float. Apply `+`, `-`, `*`,
`/`, and `%` and print each result with a label.

**Sample Input/Output:**
```
Enter first number: 10
Enter second number: 3
Sum: 13.0
Difference: 7.0
Product: 30.0
Quotient: 3.3333333333333335
Remainder: 1.0
```

---

## 4. celsius_to_fahrenheit.py
**Aim:** Convert a Celsius temperature to Fahrenheit.

**Logic:** Read Celsius as input and convert to float. Apply the formula
`F = (C * 9/5) + 32` and print the result.

**Sample Input/Output:**
```
Enter temperature in Celsius: 37
37.0°C is equal to 98.6°F
```

---

## 5. string_manipulation.py
**Aim:** Take a full name and print it in uppercase, lowercase, reversed,
and print its length.

**Logic:** Read a name string. Use `.upper()`, `.lower()`, slicing `[::-1]`
to reverse it, and `len()` for the length.

**Sample Input/Output:**
```
Enter your full name: Samarth pandit
Uppercase: SAMARTH PANDIT
Lowercase: samarth PANDIT
Reversed: tidnap htramaS
Length: 13
```

---

## 6. escape_sequence.py
**Aim:** Print a small receipt-style table using escape sequences.

**Logic:** Use `\t` to align item names and prices into columns, and `\n`
(via multiple print statements) to separate rows.

**Sample Input/Output:**
```
-------- RECEIPT --------
Item		Price
Notebook	$2.50
Pen		$1.00
Eraser		$0.50
--------------------------
Total		$4.00
```

---

## 7. calculator.py (optional)
**Aim:** A menu-driven calculator that supports add, subtract, multiply,
and divide, and keeps running until the user exits.

**Logic:** Loop indefinitely, showing a menu each time. Read the user's
choice; if it's 1–4, read two numbers and perform the matching operation
(with a divide-by-zero check). If it's 5, break out of the loop.

**Sample Input/Output:**
```
--- Menu Calculator ---
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
Choose an option (1-5): 1
Enter first number: 5
Enter second number: 3
Result: 8.0

--- Menu Calculator ---
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
Choose an option (1-5): 5
Exiting calculator. Goodbye!
```


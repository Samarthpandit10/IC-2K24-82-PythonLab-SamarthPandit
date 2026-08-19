# Lab 2

## 1. armstrong.py
**Aim:** Check whether a number is an Armstrong number, and list all
Armstrong numbers in a range.

**Logic:** Split the number into digits, raise each digit to the power of
the digit count, and sum them. If the sum equals the original number, it's
an Armstrong number. Reuse this check across a range using a list
comprehension.

**Sample Input/Output:**
```
Enter a number: 153
153 is an Armstrong number.
Enter range start: 100
Enter range end: 200
Armstrong numbers between 100 and 200: [153]
```

---

## 2. prime.py
**Aim:** Check whether a number is prime, and list all primes up to a limit.

**Logic:** A number is prime if no integer from 2 up to its square root
divides it evenly. Testing only up to the square root instead of the whole
number is enough, since any factor pair has one factor at or below the
square root.

**Sample Input/Output:**
```
Enter a number: 29
29 is prime.
Enter a limit: 30
Prime numbers up to 30: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

---

## 3. perfect_number.py
**Aim:** Check whether a number is a perfect number, and list all perfect
numbers up to a limit.

**Logic:** Sum all proper divisors of the number (numbers below it that
divide it evenly). If that sum equals the number itself, it's perfect.

**Sample Input/Output:**
```
Enter a number: 28
28 is a perfect number.
Enter a limit: 30
Perfect numbers up to 30: [6, 28]
```

---

## 4. palindrome.py
**Aim:** Check whether a number is a palindrome using only arithmetic
(no string conversion), and separately check whether a string is a
palindrome.

**Logic:** For the number version, repeatedly extract the last digit with
`% 10` and build a reversed number, then compare it to the original. For
the string version, compare the string to its reverse using slicing.

**Sample Input/Output:**
```
Enter a number: 121
121 is a palindrome number.
Enter a string: madam
"madam" is a palindrome string.
```

---

## 5. fibonacci.py
**Aim:** Print the first n Fibonacci terms using a loop, then again using
recursion, and count recursive calls.

**Logic:** The loop version keeps two running values and updates them each
iteration. The recursive version calls itself for `n-1` and `n-2` and adds
the results, with a global counter incremented on every call.

**Sample Input/Output:**
```
Enter number of terms: 10
Loop-based Fibonacci: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
Recursive Fibonacci: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
Recursive version made 276 function calls for n = 10.
```

---

## 6. pattern_printing.py
**Aim:** Print a star triangle, a number pattern, and a centered pyramid.

**Logic:** Each pattern uses a nested loop — the outer loop picks the row,
the inner loop (or string building) decides what goes on that row. The
pyramid adds leading spaces that shrink as the stars grow, keeping it
centered.

**Sample Input/Output:**
```
Enter number of rows: 4

Right-angled triangle:
*
**
***
****

Number pattern:
1
12
123
1234

Pyramid pattern:
   *
  ***
 *****
*******
```

---

## 7. menu_app.py
**Aim:** Combine programs 1–6 into a single menu-driven application that
loops until the user exits.

**Logic:** Wrap each check/pattern from programs 1–6 in its own function,
map menu numbers to those functions in a dictionary, and loop showing the
menu until the user picks the exit option. Invalid choices print a message
instead of crashing.

**Sample Input/Output:**
```
===== Menu =====
1. Check Armstrong number
...
7. Exit
Choose an option (1-7): 1
Enter a number: 153
153 is an Armstrong number.

===== Menu =====
...
Choose an option (1-7): 7
Exiting. Goodbye!
```

---

## 8. guessing_game.py
**Aim:** Let the user guess a random number between 1 and 100 within a
maximum of 7 attempts, with too-high/too-low feedback.

**Logic:** Pick a random target with `random.randint`. Loop until the user
guesses correctly or runs out of attempts, comparing each guess to the
target and giving feedback. Track and display the attempt count.

**Sample Input/Output:** (target was 82 for this run)
```
Guess a number between 1 and 100. You have 7 attempts.
Your guess: 50
Too low.
Your guess: 75
Too low.
Your guess: 88
Too high.
Your guess: 82
Correct! You guessed it in 4 attempt(s).
```

---

## Analysis

**for vs while loops:** I used `for` loops wherever the number of
iterations was known in advance — ranges in Armstrong/prime/perfect/pattern
programs, and the fixed term count in Fibonacci. I used `while` loops where
the program needed to keep running until some condition was met that
isn't tied to a counter — input validation (`get_valid_int`), the menu app
(runs until "exit" is chosen), and the guessing game (runs until a correct
guess or the attempt limit).

**Loop-based vs recursive Fibonacci:** The recursive version repeats far
more work as n grows, because it recomputes the same smaller Fibonacci
values many times over (e.g. `fib(5)` and `fib(4)` are both needed to
compute `fib(6)`, but `fib(3)` gets computed separately inside each of
those). For n = 10 it took 276 calls, while the loop version does the
same job in a single pass with no repeated work.

**Largest divisor to test for primality:** Only up to the square root of
the number. If a number `n` has a factor larger than its square root, it
must also have a matching factor smaller than the square root (since
factors pair up to multiply to `n`). So if no divisor exists up to the
square root, none exists above it either.

**Guessing game strategy:** Binary search — always guess the midpoint of
the current possible range. Each guess (via too high/too low feedback)
cuts the remaining range in half, minimizing the worst-case number of
guesses needed for any range size.


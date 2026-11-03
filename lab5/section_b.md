# Section B: Trace the Logic

## 1. ATM Simulation

Starting balance = **5000**

| Operation     | Amount | Balance |
| ------------- | -----: | ------: |
| Check Balance |      - |    5000 |
| Withdraw      |   2000 |    3000 |
| Deposit       |    500 |    3500 |
| Withdraw      |   4000 |    3500 |

The last withdrawal of **4000** should be rejected because the balance is only **3500**.

The balance remains **3500**.

---

## 2. Reverse Guessing Game

Secret number = **37**

Starting range = **1 to 100**

### First Guess

Midpoint:

`(1 + 100) // 2 = 50`

50 is too high.

New range = **1 to 49**

### Second Guess

Midpoint:

`(1 + 49) // 2 = 25`

25 is too low.

New range = **26 to 49**

### Third Guess

Midpoint:

`(26 + 49) // 2 = 37`

37 is correct.

### Trace Table

| Guess | Feedback | New Range |
| ----: | -------- | --------- |
|    50 | Too high | 1 to 49   |
|    25 | Too low  | 26 to 49  |
|    37 | Correct  | 37        |

The computer finds the number in **3 guesses**.

---

## 3. Student Grade Calculator

Marks:

* Subject 1 = 85
* Subject 2 = 92
* Subject 3 = 78
* Subject 4 = 60
* Subject 5 = 55

### Total

85 + 92 + 78 + 60 + 55 = **370**

### Average

370 / 5 = **74**

According to the grading scheme:

* 90 and above = A
* 75 to 89 = B
* 60 to 74 = C
* 40 to 59 = D
* Below 40 = F

Therefore:

**Average = 74**

**Grade = C**

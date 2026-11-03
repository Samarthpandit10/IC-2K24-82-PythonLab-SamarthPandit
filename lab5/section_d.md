# Section D: Analysis

## 1. Reverse Guessing Game

Binary search removes about half of the possible numbers after every guess. For 1 to 100, the computer can find the number in at most about 7 guesses. Checking numbers one by one could take up to 100 guesses. Therefore, binary search is much faster.

## 2. ATM Simulation

If the balance check happens after subtracting the withdrawal amount, the balance may become negative first. The program could temporarily allow an invalid transaction and then try to correct it. The correct method is to check the balance **before** subtracting the amount.

## 3. Guessing Game with Hints

Yes, the hints make the game easier. The user gets extra information about whether the secret number is even or odd and whether it is a multiple of 5. This removes some possible numbers and can reduce the expected number of guesses compared with a plain guessing game.

## 4. Combined Application

Each individual program needs its own inner loop. Instead of ending the whole program when the user chooses Exit, the program uses `break` to leave its inner loop. Control then returns to the top-level menu.

Python Star Pattern Assignment
Two Python programs that generate star patterns using nested loops and conditional logic. Both programs are dynamic — they work for any valid value of `n` and do not hard-code the pattern.
---
Question 1 — Hollow Diamond
Description
This program takes an odd number `n` from the user and prints a hollow diamond pattern made of `*` symbols. It uses nested loops to calculate the number of leading spaces and the gap between the two stars on each row, first building the upper half (including the middle row) and then mirroring it to build the lower half.
Test Case 1
Input: `n = 7`
Output:
```
   *
  * *
 *   *
*     *
 *   *
  * *
   *
```
Test Case 2
Input: `n = 5`
Output:
```
  *
 * *
*   *
 * *
  *
```
---
Question 2 — Butterfly Pattern
Description
This program takes the number of rows `n` from the user and prints a butterfly-shaped star pattern. It uses nested loops to calculate the number of stars on the left and right sides and the spaces in between for each row, building an increasing upper section and a decreasing lower section that mirrors it, meeting at a solid middle row.
Test Case 1
Input: `n = 5`
Output:
```
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
```
Test Case 2
Input: `n = 4`
Output:
```
*      *
**    **
***  ***
********
***  ***
**    **
*      *
```

Both programs use nested `for` loops and conditional statements — no manual/hard-coded print statements for individual rows.
Both programs were tested with at least two different values of `n` (shown above).
Variable names (`spaces_before`, `gap_between`, `stars`, `spaces_middle`, etc.) are chosen to clearly reflect their purpose.

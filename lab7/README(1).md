# Semester 5 — Python Dictionary Assignment

This README contains the aims, logic, sample tests, Part B output predictions, and Part C reasoning answers.

## Part A: Programs

### Q1. Student Database
**Aim:** Manage student records using nested dictionaries and generate reports.

**Logic:** Store each roll number with a name and subject-mark dictionary. A menu allows adding, updating, deleting, and viewing students. Reports calculate averages, topper, subject toppers, low marks, and grade groups.

**Sample test:** The built-in records give averages `101: 85.33`, `102: 52.33`, and `103: 74.0`. The topper is Asha. Adding roll number `101` again is rejected. Marks outside 0–100 are rejected.

### Q2. Employee Database
**Aim:** Store and manage employee details and produce department salary reports.

**Logic:** Each employee ID stores name, department, and salary. Reports calculate payroll and headcount, find the highest-paid employee per department, sort salaries, create a new dictionary with raises, and find the department with the highest average salary.

**Sample test:** IT payroll is `135000`, HR payroll is `93000`, and Finance payroll is `52000`. Dev is the highest-paid IT employee. Deleting `E9` prints `Employee not found.`

### Q3. Library Record System
**Aim:** Manage books, issuing, returns, and library reports.

**Logic:** Each ISBN stores title, author, available copies, and member IDs. The program checks availability, duplicate issues, and the two-book member limit before issuing a book.

**Sample test:** Issue B1 to M1: success, copies become 1. Issue B1 to M2: success, copies become 0. Issue B1 to M3: rejected because no copies remain. Returning B1 by M9 is rejected if M9 does not hold it.

### Q4. Word Frequency Counter
**Aim:** Count word frequencies and report word patterns from a paragraph.

**Logic:** Convert the paragraph to lowercase and replace punctuation with spaces. Count words using `.get()`, sort the most frequent words, invert frequencies, group words by length, and search for a word.

**Sample test:** Input `the cat and the hat and the bat` gives `the = 3`, `and = 2`, and `bat`, `cat`, `hat` each equal to 1. The top three are `the`, `and`, and `bat`.

### Q5. Phone Directory
**Aim:** Store contacts with multiple phone numbers and provide search and reports.

**Logic:** Each name stores phone numbers, email, and city. The program validates 10-digit numbers and rejects numbers already used by another contact. Reports provide reverse lookup, city grouping, multiple-number contacts, and alphabetical display.

**Sample test:** Searching `an` finds Anita and Manoj. Reverse lookup of `9988776655` finds Manoj. Adding Anita's number to Zara is rejected because it belongs to Anita. `12345` is rejected because it is not 10 digits.

## Part B: Predict the Output

1. `3` — `d2` and `d` refer to the same dictionary.
2. `{'x': [1, 2]}` — a shallow copy shares the nested list.
3. `{'b': 1, 'c': 2}` — zero is false, so that pair is excluded.
4. `1 5 {'a': 1, 'b': 5}` — `setdefault()` preserves existing values and inserts missing keys.
5. `{1: 'c'} 1` — `1`, `1.0`, and `True` are equal dictionary keys.
6. `RuntimeError: dictionary changed size during iteration` — the dictionary is modified while iterating.
7. `None ('b', 2)` — `pop()` uses its default for missing `z`; `popitem()` removes the last item.
8. `{1: 'b'}` — the later key overwrites the earlier key for value `1`.

## Part C: Short Reasoning

### 1. Assignment and copying
`d2 = d` creates another reference to the same dictionary. `copy()` is shallow and shares nested objects; `deepcopy()` copies nested objects too. Use `deepcopy()` if an independent copy of all nested student data is needed.

### 2. Hashable keys
Keys must be hashable so Python can find them efficiently. `(1, 2)` and `"12"` can be keys. `[1, 2]` and `{1, 2}` cannot because lists and sets are unhashable.

### 3. Dictionary access
Use `d[key]` when the key exists, `d.get(key)` when it might be missing, and `d.get(key, default)` when a fallback is needed, such as an employee-not-found message.

### 4. `.update()` and assignment
`d[key] = value` adds or changes one entry. `.update()` adds or changes multiple entries and is cleaner when applying several updates at once.

### 5. New dictionary versus in-place changes
A new comprehension preserves original salaries for comparison or recovery. In-place changes are useful when the original data should be permanently updated.

### 6. Deleting during iteration
Deleting keys while iterating changes the dictionary size and can raise `RuntimeError`. Safe methods include iterating over `list(d)` or collecting keys to delete and removing them after the loop.

### 7. Inverting library data
Loop through books and their issued member IDs, adding each title to a list for that member. Use a list because a member can hold more than one book.

### 8. Lookup complexity
Dictionary lookup is O(1) on average; list searching is O(n). A number-to-name dictionary makes phone reverse lookup faster than scanning every contact.

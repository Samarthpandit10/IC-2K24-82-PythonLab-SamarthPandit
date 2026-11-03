text = input("Enter a paragraph: ").lower()

for ch in ".,!?;:":
    text = text.replace(ch, "")

words = text.split()
count = {}

for w in words:
    count[w] = count.get(w, 0) + 1

if not words:
    print("No words entered")
else:
    print("Word count:", count)

    n = int(input("Enter top N: "))
    top = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    print("Top words:", top[:n])

    print("Words appearing once:",
          [w for w in count if count[w] == 1])

    inverse = {}
    for w, f in count.items():
        inverse.setdefault(f, []).append(w)

    for f in inverse:
        inverse[f].sort()
    print("Inverted dictionary:", inverse)

    length = {}
    for w in count:
        length.setdefault(len(w), []).append(w)
    print("Words by length:", length)

    search = input("Search a word: ").lower()
    print("Count:", count.get(search, "Not found"))

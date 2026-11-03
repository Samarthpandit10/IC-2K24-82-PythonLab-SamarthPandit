books = {
    "B1": {"title": "Python Basics", "author": "Rao", "copies": 2, "issued": []},
    "B2": {"title": "Data Structures", "author": "Iyer", "copies": 1, "issued": []},
    "B3": {"title": "Algorithms", "author": "Rao", "copies": 1, "issued": []}
}

while True:
    print("\n1.Add Book 2.Issue 3.Return 4.Search 5.Reports 6.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        i = input("Book ID: ")
        if i in books:
            books[i]["copies"] += int(input("Copies to add: "))
        else:
            books[i] = {
                "title": input("Title: "),
                "author": input("Author: "),
                "copies": int(input("Copies: ")),
                "issued": []
            }

    elif ch == 2:
        i = input("Book ID: ")
        m = input("Member ID: ")
        if i not in books:
            print("Book not found")
        elif books[i]["copies"] == 0:
            print("No copies available")
        elif m in books[i]["issued"]:
            print("Already issued")
        elif sum(m in b["issued"] for b in books.values()) >= 2:
            print("Member already has 2 books")
        else:
            books[i]["copies"] -= 1
            books[i]["issued"].append(m)
            print("Book issued")

    elif ch == 3:
        i = input("Book ID: ")
        m = input("Member ID: ")
        if i in books and m in books[i]["issued"]:
            books[i]["copies"] += 1
            books[i]["issued"].remove(m)
            print("Book returned")
        else:
            print("Invalid return")

    elif ch == 4:
        i = input("Book ID: ")
        print(books.get(i, "Book not found"))

    elif ch == 5:
        author = input("Enter author: ").lower()
        print("Books by author:",
              [b["title"] for b in books.values()
               if b["author"].lower() == author])

        members = {}
        for i, b in books.items():
            for m in b["issued"]:
                members.setdefault(m, []).append(b["title"])

        print("Members with more than one book:",
              {m: v for m, v in members.items() if len(v) > 1})

        print("Unavailable books:",
              [b["title"] for b in books.values() if b["copies"] == 0])

        print("Never issued:",
              [b["title"] for b in books.values()
               if not b["issued"]])

    elif ch == 6:
        break

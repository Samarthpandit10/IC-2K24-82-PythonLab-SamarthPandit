contacts = {
    "Anita": {"phones": ["9876543210"], "email": "anita@mail.com", "city": "Pune"},
    "Manoj": {"phones": ["9123456780", "9988776655"], "email": "manoj@mail.com", "city": "Delhi"},
    "Zara": {"phones": ["9000011111"], "email": "zara@mail.com", "city": "Pune"}
}

while True:
    print("\n1.Add 2.Add Number 3.Update 4.Delete 5.Search 6.Reports 7.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        name = input("Name: ")
        phone = input("Phone: ")
        if len(phone) == 10 and phone.isdigit():
            if any(phone in c["phones"] for c in contacts.values()):
                print("Number already exists")
            elif name not in contacts:
                contacts[name] = {
                    "phones": [phone],
                    "email": input("Email: "),
                    "city": input("City: ")
                }
            else:
                print("Contact already exists")
        else:
            print("Invalid phone number")

    elif ch == 2:
        name = input("Name: ")
        phone = input("New number: ")
        if name in contacts and len(phone) == 10 and phone.isdigit():
            if any(phone in c["phones"] for c in contacts.values()):
                print("Number already exists")
            else:
                contacts[name]["phones"].append(phone)
        else:
            print("Invalid contact or phone number")

    elif ch == 3:
        name = input("Name: ")
        if name in contacts:
            contacts[name]["email"] = input("New email: ")
            contacts[name]["city"] = input("New city: ")
        else:
            print("Contact not found")

    elif ch == 4:
        name = input("Name: ")
        if name in contacts:
            del contacts[name]
        else:
            print("Contact not found")

    elif ch == 5:
        name = input("Enter name or part of name: ").lower()
        for n, c in contacts.items():
            if name in n.lower():
                print(n, c)

    elif ch == 6:
        reverse = {p: n for n, c in contacts.items() for p in c["phones"]}
        print("Reverse lookup:", reverse)

        city = {}
        for n, c in contacts.items():
            city.setdefault(c["city"], []).append(n)
        print("Contacts by city:", city)

        print("Multiple numbers:",
              [n for n, c in contacts.items() if len(c["phones"]) > 1])

        for n in sorted(contacts):
            print(n, contacts[n])

    elif ch == 7:
        break

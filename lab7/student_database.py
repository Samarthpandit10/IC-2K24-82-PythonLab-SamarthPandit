students = {
    101: {"name": "Asha", "marks": {"Math": 88, "Physics": 76, "Chem": 92}},
    102: {"name": "Ravi", "marks": {"Math": 35, "Physics": 58, "Chem": 64}},
    103: {"name": "Meena", "marks": {"Math": 72, "Physics": 81, "Chem": 69}}
}

while True:
    print("\n1.Add 2.Update 3.Delete 4.Show 5.Reports 6.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        r = int(input("Roll number: "))
        if r in students:
            print("Roll number already exists")
        else:
            name = input("Name: ")
            marks = {}
            for sub in ["Math", "Physics", "Chem"]:
                m = int(input(sub + ": "))
                if 0 <= m <= 100:
                    marks[sub] = m
                else:
                    print("Invalid marks")
            students[r] = {"name": name, "marks": marks}

    elif ch == 2:
        r = int(input("Roll number: "))
        if r in students:
            sub = input("Subject: ")
            m = int(input("New marks: "))
            if 0 <= m <= 100:
                students[r]["marks"][sub] = m
            else:
                print("Invalid marks")
        else:
            print("Student not found")

    elif ch == 3:
        r = int(input("Roll number: "))
        if r in students:
            del students[r]
        else:
            print("Student not found")

    elif ch == 4:
        r = int(input("Roll number: "))
        print(students.get(r, "Student not found"))

    elif ch == 5:
        for r, s in students.items():
            avg = sum(s["marks"].values()) / len(s["marks"])
            print(s["name"], "Average:", round(avg, 2))

        topper = max(students, key=lambda r: sum(students[r]["marks"].values()) /
                     len(students[r]["marks"]))
        print("Topper:", students[topper]["name"])

        for sub in ["Math", "Physics", "Chem"]:
            r = max(students, key=lambda x: students[x]["marks"].get(sub, 0))
            print("Highest in", sub, ":", students[r]["name"])

        for s in students.values():
            if any(m < 40 for m in s["marks"].values()):
                print("Below 40:", s["name"])

        grades = {"A": [], "B": [], "C": [], "D": [], "F": []}
        for s in students.values():
            avg = sum(s["marks"].values()) / len(s["marks"])
            if avg >= 90: grades["A"].append(s["name"])
            elif avg >= 75: grades["B"].append(s["name"])
            elif avg >= 60: grades["C"].append(s["name"])
            elif avg >= 40: grades["D"].append(s["name"])
            else: grades["F"].append(s["name"])
        print("Grades:", grades)

    elif ch == 6:
        break

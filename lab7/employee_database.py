employees = {
    "E1": {"name": "Kiran", "dept": "IT", "salary": 60000},
    "E2": {"name": "Sara", "dept": "HR", "salary": 45000},
    "E3": {"name": "Dev", "dept": "IT", "salary": 75000},
    "E4": {"name": "Nina", "dept": "Finance", "salary": 52000},
    "E5": {"name": "Omar", "dept": "HR", "salary": 48000}
}

while True:
    print("\n1.Add 2.Update 3.Delete 4.Search 5.Reports 6.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        i = input("Employee ID: ")
        if i not in employees:
            employees[i] = {
                "name": input("Name: "),
                "dept": input("Department: "),
                "salary": int(input("Salary: "))
            }
        else:
            print("ID already exists")

    elif ch == 2:
        i = input("Employee ID: ")
        if i in employees:
            employees[i]["salary"] = int(input("New salary: "))
        else:
            print("Employee not found")

    elif ch == 3:
        i = input("Employee ID: ")
        if i in employees:
            del employees[i]
        else:
            print("Employee not found")

    elif ch == 4:
        i = input("Employee ID: ")
        print(employees.get(i, "Employee not found"))

    elif ch == 5:
        dept = {}
        for i, e in employees.items():
            d = e["dept"]
            if d not in dept:
                dept[d] = {"total": 0, "count": 0}
            dept[d]["total"] += e["salary"]
            dept[d]["count"] += 1

        for d, v in dept.items():
            print(d, "Payroll:", v["total"], "Employees:", v["count"])

            top = max([e for e in employees.values() if e["dept"] == d],
                      key=lambda x: x["salary"])
            print("Highest paid:", top["name"])

        print("Salary order:")
        for e in sorted(employees.values(), key=lambda x: x["salary"], reverse=True):
            print(e["name"], e["salary"])

        # A new dictionary keeps the original salaries unchanged.
        new = {i: e["salary"] * 1.1 if e["salary"] < 50000 else e["salary"]
               for i, e in employees.items()}
        print("After raise:", new)

        avg = {d: v["total"] / v["count"] for d, v in dept.items()}
        print("Highest average salary:", max(avg, key=avg.get))

    elif ch == 6:
        break

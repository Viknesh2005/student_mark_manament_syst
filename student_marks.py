# hello
students = {}

def add_student(name):
    students[name] = []

def add_mark(name, mark):
    if name in students:
        students[name].append(mark)
        print(f"Mark {mark} added for {name}.")
    else:
        print(f"Student {name} not found.")

def calculate_average(name):
    if name in students and students[name]:
        average = sum(students[name]) / len(students[name])
        print(f"Average mark for {name}: {average:.2f}")
    else:
        print(f"No marks found for {name}.")

while True:
    print("\n1. Add student")
    print("2. Add marks for a student")
    print("3. Calculate average for a student")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        name = input("Enter student name: ")
        add_student(name)
        print(f"Student {name} added.")

    elif choice == '2':
        name = input("Enter student name: ")
        mark = float(input("Enter mark: "))
        add_mark(name, mark)

    elif choice == '3':
        name = input("Enter student name: ")
        calculate_average(name)

    elif choice == '4':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")




def add_student(students):
    name = input("Enter student name: ")
    math_mark = float(input("Enter Your Maths Marks: "))
    sci_mark = float(input("Enter Your Science Marks: "))
    students.append({"name": name, "math" : math_mark, "sci" : sci_mark})
    print("Student added!")


def display_students(students):
    if not students:
        print("No Students Yet")
    else:
        print("Students and Marks")

        for s in students:
            print(f"{s['name']} - {s['math']} - {s['sci']}")




students = []

while True:
    print("\nWelcome to Student Marks Manager")
    print("1. Add student")
    print("2. Display all students")
    print("3. Show average marks")
    print("4. Show top and bottom scorer")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student(students)
    elif choice == "2":
        display_students(students)
    elif choice == "3":
        print("not developped yet")
    elif choice == "4":
        print("not developped yet")
    elif choice == "5":
        print("Good Bye!")
        break
    else:
        print("Invalid Choice, Please Try Again")
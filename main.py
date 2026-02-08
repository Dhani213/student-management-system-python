# Student Management System(This program is used to manage student records such as roll number, name, course, and marks.)



FILE_NAME = "students.txt" #(This is the file name where our data will be stored.)

def show_menu():
    print("\n ~Student Management System~ ")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

def get_valid_roll(): #(This function is created just to check whether the entered roll no. is valid i.e. consist only of digits.)
    while True:
        roll = input("Please enter a valid Roll Number: ")
        if roll.isdigit():
            return roll
        else:
            print("Attention!! Roll number must contain only digits!")


def get_valid_name(): #(This function is created just to check whether the entered name is valid i.e. consist only of letters.)
    while True:
        name = input("Please enter your Name: ")
        if name.replace(" ", "").isalpha():
            return name
        else:
            print("Attention!! Name should contain only letters!")


def get_valid_course(): #(This function is created just to check whether the entered course is valid or not.)
    while True:
        course = input("Please enter Course: ").strip()
        if course:
            return course
        else:
            print("Attention!! Course cannot be empty!")


def get_valid_marks(): #(This function is created just to check whether the entered marks are valid i.e. should be between 0 to 100.)
    while True:
        marks = input("Please enter Marks (0-100): ")
        if marks.isdigit() and 0 <= int(marks) <= 100:
            return marks
        else:
            print("Attention!! Marks must be between 0 and 100!")


def roll_exists(check_roll): #(This function is created just to check whether the entered roll no. exists in the file or not.)
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                roll = line.strip().split(",")[0]
                if roll == check_roll:
                    return True
    except FileNotFoundError:
        return False
    return False

#(Ok, now these are the core features that are being added now from here.)
def add_student():
    print("\n Add Student ")

    while True:
        roll = get_valid_roll()
        if roll_exists(roll):
            print("Attention!! Roll number already exists! Try another.")
        else:
            break

    name = get_valid_name()
    course = get_valid_course()
    marks = get_valid_marks()

    with open(FILE_NAME, "a") as file:
        file.write(f"{roll},{name},{course},{marks}\n")

    print("Attention!!  Student added successfully!")


def view_students():
    print("\n Student Records ")

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

            if not lines:
                print("Attention!! No student records found.")
                return

            print("Roll | Name | Course | Marks")
            print("-------------------------------")

            for line in lines:
                roll, name, course, marks = line.strip().split(",")
                print(f"{roll} | {name} | {course} | {marks}")

    except FileNotFoundError:
        print("Attention!! Student file not found!")


def search_student():
    print("\n Search Student ")
    search_roll = get_valid_roll()

    found = False

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                roll, name, course, marks = line.strip().split(",")

                if roll == search_roll:
                    print("\n Hurray!! Student Found:")
                    print(f"Roll   : {roll}")
                    print(f"Name   : {name}")
                    print(f"Course : {course}")
                    print(f"Marks  : {marks}")
                    found = True
                    break

        if not found:
            print("Oops!! Student not found!")

    except FileNotFoundError:
        print("Attention!! Student file not found!")


def update_student():
    print("\ Update Student ")
    update_roll = get_valid_roll()

    students = []
    updated = False

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                roll, name, course, marks = line.strip().split(",")

                if roll == update_roll:
                    print("\n Current Details: ")
                    print(f"Name   : {name}")
                    print(f"Course : {course}")
                    print(f"Marks  : {marks}")

                    print("\n Enter New Details: ")
                    new_name = get_valid_name()
                    new_course = get_valid_course()
                    new_marks = get_valid_marks()

                    students.append(f"{roll},{new_name},{new_course},{new_marks}\n")
                    updated = True
                else:
                    students.append(line)

        if updated:
            with open(FILE_NAME, "w") as file:
                file.writelines(students)
            print("Hurray!! Student record updated successfully!")
        else:
            print("Oops!! Student not found!")

    except FileNotFoundError:
        print("Attention!! Student file not found!")


def delete_student():
    print("\n Delete Student ")
    delete_roll = get_valid_roll()

    students = []
    deleted = False

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                roll, name, course, marks = line.strip().split(",")

                if roll == delete_roll:
                    print("\n Student to be deleted: ")
                    print(f"Name   : {name}")
                    print(f"Course : {course}")
                    print(f"Marks  : {marks}")

                    confirm = input("Confirm delete? (y/n): ").lower()
                    if confirm == "y":
                        deleted = True
                        continue
                    else:
                        students.append(line)
                else:
                    students.append(line)

        if deleted:
            with open(FILE_NAME, "w") as file:
                file.writelines(students)
            print("Hurray!! Student record deleted successfully!")
        else:
            print("Oops!! Student not found or deletion cancelled!")

    except FileNotFoundError:
        print("Attention!! Student file not found!")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")

        if not choice.isdigit():
            print("Attention!! Please enter numbers only!")
            continue

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting program. Thank you!")
            break
        else:
            print("Attention!! Invalid choice! Enter between 1 and 6.")

        input("\n Press Enter to return to menu ")


#(Main program starts here)
main()

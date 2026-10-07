print("Welcome To Student Management System")

students = {}
student_id = 1

while True:

    print("\n1. Add student")
    print("2. Remove student")
    print("3. Search student")
    print("4. Update marks")
    print("5. Display all students")
    print("6. Show topper")
    print("7. Show average marks")
    print("8. Save data")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        # 1. Add student
        case 1:
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            marks = float(input("Enter student marks: "))

            students[student_id] = {
                "name": name,
                "age": age,
                "marks": marks
            }

            print(f"Student added successfully! Student ID: {student_id}")

            student_id += 1

        # 2. Remove student
        case 2:
            remove_student = int(input("Enter the student ID to remove: "))

            if remove_student not in students:
                print("That ID does not exist.")
            else:
                students.pop(remove_student)
                print("Student removed successfully.")

        # 3. Search student
        case 3:
            search = int(input("Enter student ID to search: "))

            if search not in students:
                print("That ID does not exist.")
            else:
                print(students[search])

        # 4. Update marks
        case 4:
            which_student = int(
                input("Enter student ID whose marks you want to update: ")
            )

            if which_student not in students:
                print("That ID does not exist.")
            else:
                update_marks = float(
                    input("Enter new marks: ")
                )

                students[which_student]["marks"] = update_marks

                print("Marks updated successfully.")

        # 5. Display all students
        case 5:
            if not students:
                print("No students available.")
            else:
                for student_id, student in students.items():
                    print(
                        f"ID: {student_id}, "
                        f"Name: {student['name']}, "
                        f"Age: {student['age']}, "
                        f"Marks: {student['marks']}"
                    )

        # 6. Show topper
        case 6:
            if not students:
                print("No students available.")
            else:
                topper_id = max(
                    students,
                    key=lambda student_id: students[student_id]["marks"]
                )

                print("Topper:")
                print("ID:", topper_id)
                print("Name:", students[topper_id]["name"])
                print("Marks:", students[topper_id]["marks"])

        # 7. Show average marks
        case 7:
            if not students:
                print("No students available.")
            else:
                total_marks = 0

                for student in students.values():
                    total_marks += student["marks"]

                average = total_marks / len(students)

                print("Average marks:", average)

        # 8. Save data
        case 8:
            print("Student data:")
            print(students)

        # 9. Exit
        case 9:
            print("Thank you for using Student Management System!")
            break

        case _:
            print("Invalid choice. Please enter 1-9.")
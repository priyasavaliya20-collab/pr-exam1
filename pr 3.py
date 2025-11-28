print("Welcome to the Student Data Organizer!")

students = []

while True:
    print("\n===== Main Menu =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nEnter student details:")
        student_id = input("Student ID: ")
        full_name = input("Name: ")

        while True:
            age = input("Age: ")
            if age.isdigit():
                break
            print("Invalid age! Enter a number.")

        grade_level = input("Grade: ")
        birth_date = input("Date of Birth (YYYY-MM-DD): ")
        subjects_input = input("Subjects : ")

        new_student = {
            "id": student_id,
            "name": full_name,
            "age": age,
            "grade": grade_level,
            "dob": birth_date,
            "subjects": subjects_input
        }

        students.append(new_student)
        print("Student added successfully!")

    elif choice == "2":
        print("\n===== Student Records =====")
        if not students:
            print("No students found.")
        else:
            for student in students:
                print("ID:", student["id"],
                      "| Name:", student["name"],
                      "| Age:", student["age"],
                      "| Grade:", student["grade"],
                      "| DOB:", student["dob"],
                      "| Subjects:", student["subjects"])

    elif choice == "3":
        update_id = input("\nEnter Student ID to update: ")
        student_found = False

        for student in students:
            if student["id"] == update_id:
                print("\nEnter new details :")

                new_name = input(f"Name ({student['name']}): ")
                new_age = input(f"Age ({student['age']}): ")
                new_grade = input(f"Grade ({student['grade']}): ")
                new_dob = input(f"DOB ({student['dob']}): ")
                new_subjects = input("Subjects (comma-separated): ")

                if new_name:
                    student["name"] = new_name
                if new_age:
                    student["age"] = new_age
                if new_grade:
                    student["grade"] = new_grade
                if new_dob:
                    student["dob"] = new_dob
                if new_subjects:
                    student["subjects"] = new_subjects

                print("Student updated successfully!")
                student_found = True
                break

        if not student_found:
            print("Student not found.")

    elif choice == "4":
        delete_id = input("\nEnter Student ID to delete: ")
        deleted = False

        for student in students:
            if student["id"] == delete_id:
                students.remove(student)
                print("Student deleted successfully!")
                deleted = True
                break

        if not deleted:
            print("Student not found.")

        elif choice == "5":
          print("\n--- Subjects Offered ---")
        
        if not student:
            print("No subjects available.")
        else:
            subjects = set()
            for s in student:
                subjects.add(s["subjects"])   
            
            for sub in subjects:
                print(sub)

    elif choice == "6":
        print("\nThank you for using the Student Data Organizer! Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")

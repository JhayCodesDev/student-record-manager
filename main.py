from student_manager import StudentRecordManager

def valid_name():
    # Request a non-empty student name.

    while True:
        name = input("Enter student name: ").strip()

        if name and any(character.isalpha() for character in name):
            return name

        print("Please enter a valid name.")

def valid_id():
     # Request a non-empty student ID.

    while True:
        student_id = input("Enter student ID: ").strip()

        if student_id:
            return student_id

        print("Student ID cannot be empty.")

def valid_subject_name():
    # Request a non-empty subject name.

    while True:
        subject = input("Enter subject name: ").strip()

        if subject:
            return subject

        print("Subject name cannot be empty.")

def valid_subject_length():
    # Request a subject count between 1 and 10.

    while True:
        try:
            subject_length = int(input("Enter number of subjects (1-10): "))

            if 1 <= subject_length <= 10:
                return subject_length

            print("Subject count must be between 1 and 10.")

        except ValueError:
            print("Please enter a valid whole number.")

def valid_score():
    # Request a score between 0 and 100.

    while True:
        try:
            score = float(input("Enter subject score (0-100): "))

            if 0 <= score <= 100:
                return score

            print("Score must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid numeric score.")

def valid_user_choice(minimum, maximum):
    # Request a menu choice within the allowed range.

    while True:
        try:
            choice = int(input("Choose an option: "))

            if minimum <= choice <= maximum:
                return choice

            print(f"Choose an option between {minimum} and {maximum}.")

        except ValueError:
            print("Please enter a valid whole number.")

def collect_subjects():
    # Collect subject names and scores.

    subject_count = valid_subject_length()
    subjects = {}

    for number in range(1, subject_count + 1):
        print(f"\nSubject {number}")

        subject_name = valid_subject_name()

        while subject_name in subjects:
            print("That subject has already been entered.")
            subject_name = valid_subject_name()

        subjects[subject_name] = valid_score()

    return subjects

def display_student(student):
    # Display an individual student's record.

    print("\n--- Student Record ---")
    print(f"Name: {student.name}")
    print(f"Student ID: {student.student_id}")

    if student.subjects:
        print("Subjects and scores:")

        for subject, score in student.subjects.items():
            print(f"  {subject}: {score:g}")

        average = student.calculate_average()

        print(f"Average score: {average:.2f}")
        print(f"Grade: {student.calculate_grade()}")

    else:
        print("No subject scores available.")

    print("----------------------")

def add_student(manager):
    # Collect and register a new student.

    print("\n--- Add Student ---")

    name = valid_name()
    student_id = valid_id()
    subjects = collect_subjects()

    try:
        student = manager.add_student(name, student_id, subjects)

        print(f"\nStudent '{student.name}' added successfully.")

    except ValueError as error:
        print(f"\nUnable to add student: {error}")

    except OSError as error:
        print(f"\nUnable to save the student record: {error}")

def view_unique_student_record(manager):
    # Find and display one student.

    print("\n--- View Student Record ---")

    student_id = valid_id()
    student = manager.find_student(student_id)

    if student is None:
        print("Student not found.")
        return

    display_student(student)

def view_all_student_records(manager):
    # Display every stored student record.

    print("\n--- All Student Records ---")

    students = manager.get_all_students()

    if not students:
        print("No student records found.")
        return

    for student in students:
        display_student(student)

def calculate_all_averages(manager):
    # Display averages and grades for every student.

    print("\n--- Student Averages ---")

    students = manager.get_all_students()

    if not students:
        print("No student records found.")
        return

    for student in students:
        print(f"\nStudent Name: {student.name}")
        print(f"Student ID: {student.student_id}")

        average = student.calculate_average()

        if average is None:
            print("Average Score: N/A")
            print("Student Grade: N/A")
        else:
            print(f"Average Score: {average:.2f}")
            print(f"Student Grade: {student.calculate_grade()}")

def edit_student_record(manager):
    # Edit an existing student's information.

    print("\n--- Edit Student Record ---")

    student_id = valid_id()
    student = manager.find_student(student_id)

    if student is None:
        print("Student not found.")
        return

    while True:
        print("\nWhat would you like to edit?")
        print("1. Student Name")
        print("2. Student ID")
        print("3. Subject Scores")
        print("4. Return to Main Menu")

        choice = valid_user_choice(1, 4)

        try:
            if choice == 1:
                new_name = valid_name()

                manager.update_student(
                    student_id,
                    name=new_name,
                )

                print("Student name updated successfully.")

            elif choice == 2:
                new_id = valid_id()

                manager.update_student(
                    student_id,
                    new_student_id=new_id,
                )

                student_id = new_id

                print("Student ID updated successfully.")

            elif choice == 3:
                new_subjects = collect_subjects()

                manager.update_student(
                    student_id,
                    subjects=new_subjects,
                )

                print("Subject scores updated successfully.")

            else:
                return

        except ValueError as error:
            print(f"Unable to update record: {error}")

        except OSError as error:
            print(f"Unable to save changes: {error}")

def delete_student_record(manager):
    # Delete a student's record after confirmation.

    print("\n--- Delete Student Record ---")

    student_id = valid_id()
    student = manager.find_student(student_id)

    if student is None:
        print("Student not found.")
        return

    display_student(student)

    confirmation = input(
        "Are you sure you want to delete this student? (y/n): "
    ).strip().lower()

    if confirmation != "y":
        print("Deletion cancelled.")
        return

    try:
        manager.delete_student(student_id)

        print("Student record deleted successfully.")

    except ValueError as error:
        print(f"Unable to delete record: {error}")

    except OSError as error:
        print(f"Unable to save the deletion: {error}")

def display_menu():
    # Display the main application menu.

    print("\n========== Student Record Manager ==========")
    print("1. Add a new student")
    print("2. View an individual student record")
    print("3. View all student records")
    print("4. Calculate student average scores")
    print("5. Edit a student record")
    print("6. Delete a student record")
    print("7. Exit")
    print("============================================")

def main():
    try:
        manager = StudentRecordManager()

    except (RuntimeError, OSError) as error:
        print(f"\nUnable to initialize Student Record Manager: {error}")
        return

    print("\nWelcome to Student Record Manager!")

    while True:
        display_menu()
        choice = valid_user_choice(1, 7)

        if choice == 1:
            add_student(manager)

        elif choice == 2:
            view_unique_student_record(manager)

        elif choice == 3:
            view_all_student_records(manager)

        elif choice == 4:
            calculate_all_averages(manager)

        elif choice == 5:
            edit_student_record(manager)

        elif choice == 6:
            delete_student_record(manager)

        elif choice == 7:
            print("\nThanks for using Student Record Manager!")
            break

if __name__ == '__main__':
    main()

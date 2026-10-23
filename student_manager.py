from pathlib import Path
import json

from student import Student

class StudentRecordManager:
      # Manage student records and persist them in a JSON file.

    def __init__(self, file_path="student_record.json"):
        self.file_path = Path(file_path)
        self.students = []

        self.load_records()

    def load_records(self):
        # Load student records from the JSON file.

        if not self.file_path.exists():
            self.students = []
            self.save_records()
            return

        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, list):
                raise ValueError("The record file must contain a JSON list.")

            loaded_students = []

            for item in data:
                if not isinstance(item, dict):
                    raise ValueError("Each student record must be an object.")

                name = item["name"]
                student_id = item["id"]
                subjects = item["subjects"]

                if not isinstance(name, str) or not name.strip():
                    raise ValueError("A student name is missing or invalid.")

                if not isinstance(student_id, str) or not student_id.strip():
                    raise ValueError("A student ID is missing or invalid.")

                if not isinstance(subjects, dict):
                    raise ValueError("Student subjects must be a dictionary.")

                validated_subjects = {}

                for subject, score in subjects.items():
                    if not isinstance(subject, str) or not subject.strip():
                        raise ValueError("A subject name is missing or invalid.")

                    if (
                        isinstance(score, bool)
                        or not isinstance(score, (int, float))
                        or not 0 <= score <= 100
                    ):
                        raise ValueError(
                            f"Invalid score stored for subject: {subject}"
                        )

                    validated_subjects[subject] = score

                loaded_students.append(
                    Student(
                        name=name,
                        student_id=student_id,
                        subjects=validated_subjects,
                    )
                )

            student_ids = [
                student.student_id for student in loaded_students
            ]

            if len(student_ids) != len(set(student_ids)):
                raise ValueError("Duplicate student IDs were found.")

            self.students = loaded_students

        except (json.JSONDecodeError, OSError, ValueError, KeyError) as error:
            raise RuntimeError(
                f"Unable to load student records: {error}"
            ) from error

    def save_records(self):
        # Save all student records to the JSON file.

        data = [student.to_dict() for student in self.students]

        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def find_student(self, student_id):
        # Return a student object matching the given ID, or None.

        for student in self.students:
            if student.student_id == student_id:
                return student

        return None

    def add_student(self, name, student_id, subjects):
        # Add a student if the student ID is not already in use.

        if self.find_student(student_id) is not None:
            raise ValueError("A student with this ID already exists.")

        student = Student(
            name=name,
            student_id=student_id,
            subjects=subjects,
        )

        self.students.append(student)

        try:
            self.save_records()
        except OSError:
            self.students.remove(student)
            raise

        return student

    def get_all_students(self):
        # Return the collection of student objects.

        return list(self.students)

    def update_student(self, student_id, name=None, new_student_id=None,
                       subjects=None):
        # Update the details of an existing student.

        student = self.find_student(student_id)

        if student is None:
            raise ValueError("Student not found.")

        if new_student_id is not None:
            existing_student = self.find_student(new_student_id)

            if existing_student is not None and existing_student is not student:
                raise ValueError("That student ID is already in use.")

        old_name = student.name
        old_id = student.student_id
        old_subjects = student.subjects

        if name is not None:
            student.name = name

        if new_student_id is not None:
            student.student_id = new_student_id

        if subjects is not None:
            student.subjects = subjects

        try:
            self.save_records()
        except OSError:
            student.name = old_name
            student.student_id = old_id
            student.subjects = old_subjects
            raise

        return student

    def delete_student(self, student_id):
        # Delete a student and save the updated records.

        student = self.find_student(student_id)

        if student is None:
            raise ValueError("Student not found.")

        self.students.remove(student)

        try:
            self.save_records()
        except OSError:
            self.students.append(student)
            raise

        return student
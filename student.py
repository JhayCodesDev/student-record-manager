class Student:
## Represent an individual student and their academic records.

    def __init__(self, name, student_id, subjects=None):
        self.name = name
        self.student_id = student_id
        self.subjects = subjects if subjects is not None else {}

    def calculate_average(self):
        # Calculate the student's average score.

        if not self.subjects:
            return None

        total_score = sum(self.subjects.values())
        subject_count = len(self.subjects)

        return total_score / subject_count

    def calculate_grade(self):
        # Calculate the student's grade using the average score.

        average = self.calculate_average()

        if average is None:
            return "N/A"

        if average >= 70:
            return "A"
        elif average >= 60:
            return "B"
        elif average >= 50:
            return "C"
        elif average >= 45:
            return "D"
        elif average >= 40:
            return "E"
        else:
            return "F"

    def to_dict(self):
        # Convert the student object into a JSON-compatible dictionary.

        return {
            "name": self.name,
            "id": self.student_id,
            "subjects": self.subjects,
        }

    @classmethod
    def from_dict(cls, data):
        # Create a Student object from a stored dictionary.

        return cls(
            name=data["name"],
            student_id=data["id"],
            subjects=data["subjects"],
        )

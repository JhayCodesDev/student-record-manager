# Student Record Manager

A command-line application built with Python for managing student records, subject scores, averages, and grades. The application uses object-oriented programming (OOP) to organize student data and JSON for persistent local storage.

## Overview

The Student Record Manager allows users to create and manage student records through an interactive command-line menu.

The project was built to strengthen my understanding of Python fundamentals, object-oriented programming, input validation, file handling, and data persistence while solving a practical problem.

## Features

* **Add Students:** Register students with unique IDs, names, and subject scores.
* **View Individual Records:** Search for a student using their ID and display their academic information.
* **View All Records:** Display all registered students and their academic results.
* **Calculate Averages:** Calculate each student's average score across their subjects.
* **Assign Grades:** Automatically assign grades based on students' average scores.
* **Edit Records:** Update student names, IDs, and subject scores.
* **Delete Records:** Remove student records with confirmation.
* **Input Validation:** Handle invalid menu choices, empty fields, and invalid numeric input.
* **Duplicate ID Prevention:** Prevent multiple students from being registered with the same student ID.
* **Persistent Storage:** Store student records in a JSON file so that data remains available between application sessions.

## Technologies Used

* **Python** — Application logic and object-oriented programming.
* **JSON** — Local data storage.
* **pathlib** — File and path management.
* **Git and GitHub** — Version control and project hosting.

The application uses Python's standard library and does not require third-party packages.

## Project Structure

```text
student-record-manager/
│
├── main.py
├── student.py
├── student_manager.py
├── student_record.json
└── README.md
```

### File Responsibilities

| File                  | Description                                                                                                                 |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `main.py`             | Application entry point, interactive menu, input validation, and user interaction.                                          |
| `student.py`          | Defines the `Student` class and its methods for calculating averages, assigning grades, and converting student data.        |
| `student_manager.py`  | Defines the `StudentRecordManager` class, which manages student records and JSON persistence.                               |
| `student_record.json` | Stores student records locally in JSON format. Created automatically when the application initializes if it does not exist. |
| `README.md`           | Project documentation.                                                                                                      |

## Getting Started

### Prerequisites

Ensure Python 3 is installed on your computer.

Check your Python installation by running:

```bash
python --version
```

If your system uses `python3`, run:

```bash
python3 --version
```

No additional Python packages are required.

### Installation

**1. Clone the repository**

Replace `<your-github-username>` with your actual GitHub username.

```bash
git clone https://github.com/JhayCodesDev/student-record-manager.git
```

**2. Navigate to the project directory**

```bash
cd student-record-manager
```

**3. Run the application**

```bash
python main.py
```

Alternatively:

```bash
python3 main.py
```

The application will initialize the record manager, load any existing student records, and display the main menu.

## How to Use

When the application starts, the following menu is displayed:

```text
========== Student Record Manager ==========
1. Add a new student
2. View an individual student record
3. View all student records
4. Calculate student average scores
5. Edit a student record
6. Delete a student record
7. Exit
============================================
```

Enter the number corresponding to the operation you want to perform.

### Adding a Student

Select option `1` and provide the student's name, unique student ID, number of subjects, and subject scores.

The application validates the input, checks that the student ID is not already in use, and saves the record.

### Viewing a Student Record

Select option `2` and enter the student's ID.

If the student exists, the application displays their name, ID, subjects, scores, average, and grade.

### Viewing All Student Records

Select option `3` to display all registered students and their academic information.

### Calculating Average Scores

Select option `4` to display each student's average score and corresponding grade.

The average is calculated using:

**Average Score = Total Score / Number of Subjects**

For example, if a student scores 80, 70, and 90:

```text
Average = (80 + 70 + 90) / 3
Average = 80
```

### Editing a Student Record

Select option `5` to update a student's name, ID, or subject scores.

Changes are saved to the JSON file.

### Deleting a Student Record

Select option `6`, enter the student's ID, and confirm the deletion.

The record is removed from the collection and the updated data is saved.

### Exiting the Application

Select option `7` to exit the program.

## Grading System

The application uses the following grading boundaries:

| Average Score   | Grade |
| --------------- | ----- |
| 70–100          | A     |
| 60–less than 70 | B     |
| 50–less than 60 | C     |
| 45–less than 50 | D     |
| 40–less than 45 | E     |
| Below 40        | F     |

These boundaries are configurable in the `calculate_grade()` method in `student.py`.

The grading system is intended for this project and should be adjusted if a different institution's grading policy is required.

## Data Storage

Student records are stored locally in `student_record.json`.

Each record follows this structure:

```json
[
    {
        "name": "Joshua",
        "id": "CU001",
        "subjects": {
            "Mathematics": 85,
            "English": 78,
            "Physics": 90
        }
    }
]
```

The application loads records into Python objects when it starts and saves changes to the JSON file.

**Important:** The JSON file is local to the project. Back up the file if you need to preserve your records, and avoid manually editing it into an invalid JSON structure.

## Key Concepts Practised

This project provides practical experience with:

* **Object-Oriented Programming:** Creating classes and objects to represent students and manage records.
* **Functions and Methods:** Organizing application logic into reusable components.
* **Input Validation:** Handling invalid user input and enforcing application rules.
* **Exception Handling:** Managing common input and file-loading errors.
* **File Handling:** Reading and writing persistent data.
* **JSON Serialization:** Converting Python objects into JSON-compatible data and reconstructing objects from stored dictionaries.
* **Data Structures:** Working with lists and dictionaries.
* **Searching and Updating Data:** Finding records by ID and modifying existing student information.
* **Separation of Concerns:** Organizing the application into modules with distinct responsibilities.

## Future Improvements

Potential enhancements include:

* Adding automated unit tests.
* Introducing a graphical user interface.
* Supporting CSV export and import.
* Adding student ranking and performance summaries.
* Supporting additional grading systems.
* Migrating from JSON storage to SQLite as the application grows.
* Improving data recovery and file-write reliability.

## Learning Objectives

The goal of this project is not only to create a functional student record system but also to understand how Python concepts work together in a practical application.

It provides an opportunity to practise writing maintainable code, debugging logical errors, validating input, organizing responsibilities, and managing persistent data.

## Author

**JhayCodes**

GitHub: [https://github.com/JhayCodesDev]

Portfolio: [https://jhaycodesdev.vercel.app]

---

*Built with Python, curiosity, and a commitment to learning by understanding how things work.*

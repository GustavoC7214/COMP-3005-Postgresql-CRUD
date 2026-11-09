"""
Main application for the COMP 3005 PostgreSQL CRUD assignment.

Provides an interactive command-line menu for performing
Create, Read, Update, and Delete operations on students.
"""

from datetime import date

from app.database import (
    addStudent,
    deleteStudent,
    getAllStudents,
    updateStudentEmail,
)


def display_menu():
    """Display the available database operations."""
    print("\n====================================")
    print(" Student Database Management System")
    print("====================================")
    print("1. View all students")
    print("2. Add a student")
    print("3. Update student email")
    print("4. Delete a student")
    print("5. Exit")
    print("====================================")


def get_student_id():
    """Prompt for a valid positive student ID."""
    try:
        student_id = int(input("Enter student ID: ").strip())

        if student_id <= 0:
            print("Error: Student ID must be positive.")
            return None

        return student_id

    except ValueError:
        print("Error: Student ID must be an integer.")
        return None


def handle_add_student():
    """Collect student details and insert a new record."""
    print("\n--- Add Student ---")

    first_name = input("First name: ").strip()
    last_name = input("Last name: ").strip()
    email = input("Email: ").strip()
    enrollment_date = input("Enrollment date (YYYY-MM-DD): ").strip()

    # Validate required fields before querying PostgreSQL.
    if not first_name or not last_name or not email:
        print("Error: First name, last name, and email are required.")
        return

    # Validate the date format.
    try:
        date.fromisoformat(enrollment_date)
    except ValueError:
        print("Error: Enrollment date must use YYYY-MM-DD format.")
        return

    addStudent(first_name, last_name, email, enrollment_date)


def handle_update_email():
    """Collect a student ID and their new email address."""
    print("\n--- Update Student Email ---")

    student_id = get_student_id()

    if student_id is None:
        return

    new_email = input("Enter new email: ").strip()

    if not new_email:
        print("Error: Email cannot be empty.")
        return

    updateStudentEmail(student_id, new_email)


def handle_delete_student():
    """Collect a student ID and request confirmation before deletion."""
    print("\n--- Delete Student ---")

    student_id = get_student_id()

    if student_id is None:
        return

    confirmation = (
        input(f"Are you sure you want to delete student {student_id}? (y/n): ")
        .strip()
        .lower()
    )

    if confirmation == "y":
        deleteStudent(student_id)
    else:
        print("Deletion cancelled.")


def main():
    """Run the application until the user chooses to exit."""
    while True:
        display_menu()

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            getAllStudents()

        elif choice == "2":
            handle_add_student()

        elif choice == "3":
            handle_update_email()

        elif choice == "4":
            handle_delete_student()

        elif choice == "5":
            print("Exiting application. Goodbye!")
            break

        else:
            print("Invalid choice. Please select an option from 1 to 5.")


if __name__ == "__main__":
    main()

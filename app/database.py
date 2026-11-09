import os
from datetime import date

import psycopg
from psycopg import errors

# PostgreSQL connection settings.
# Environment variables allow users to configure their own database.
DB_CONFIG = {
    "dbname": os.getenv("DB_NAME", "student_db"),
    "user": os.getenv("DB_USER", os.getenv("USER")),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", "5432")),
    "password": os.getenv("DB_PASSWORD") or None,
}


def get_connection():
    """Create and return a connection to the PostgreSQL database."""
    return psycopg.connect(**DB_CONFIG)


def getAllStudents():
    """Retrieve and display all students ordered by student ID."""
    try:
        with get_connection() as conn, conn.cursor() as cursor:
            cursor.execute(
                """
                    SELECT student_id, first_name, last_name,
                           email, enrollment_date
                    FROM students
                    ORDER BY student_id;
                    """
            )
            students = cursor.fetchall()

        if not students:
            print("No students found.")
            return

        print("\n--- All Students ---")

        for student in students:
            student_id, first_name, last_name, email, enrollment_date = student

            print(
                f"ID: {student_id} | "
                f"Name: {first_name} {last_name} | "
                f"Email: {email} | "
                f"Enrollment Date: {enrollment_date}"
            )

    except psycopg.Error as error:
        print(f"Error retrieving students: {error}")


def addStudent(first_name, last_name, email, enrollment_date):
    """Insert a new student into the database."""
    try:
        # Validate the enrollment date before inserting.
        if isinstance(enrollment_date, str):
            enrollment_date = date.fromisoformat(enrollment_date)

        with get_connection() as conn, conn.cursor() as cursor:
            cursor.execute(
                """
                    INSERT INTO students (
                        first_name, last_name, email, enrollment_date
                    )
                    VALUES (%s, %s, %s, %s)
                    RETURNING student_id;
                    """,
                (first_name, last_name, email, enrollment_date),
            )

            student_id = cursor.fetchone()[0]

        print(f"Student added successfully with ID {student_id}.")

    except errors.UniqueViolation:
        print("Error: A student with this email already exists.")

    except ValueError:
        print("Error: Enrollment date must use YYYY-MM-DD format.")

    except psycopg.Error as error:
        print(f"Error adding student: {error}")


def updateStudentEmail(student_id, new_email):
    """Update the email address of an existing student."""
    try:
        with get_connection() as conn, conn.cursor() as cursor:
            cursor.execute(
                """
                    UPDATE students
                    SET email = %s
                    WHERE student_id = %s;
                    """,
                (new_email, student_id),
            )

            updated_rows = cursor.rowcount

        if updated_rows == 0:
            print(f"No student found with ID {student_id}.")
        else:
            print(f"Email updated successfully for student {student_id}.")

    except errors.UniqueViolation:
        print("Error: This email is already assigned to another student.")

    except psycopg.Error as error:
        print(f"Error updating student email: {error}")


def deleteStudent(student_id):
    """Delete a student from the database using their student ID."""
    try:
        with get_connection() as conn, conn.cursor() as cursor:
            cursor.execute(
                """
                    DELETE FROM students
                    WHERE student_id = %s;
                    """,
                (student_id,),
            )

            deleted_rows = cursor.rowcount

        if deleted_rows == 0:
            print(f"No student found with ID {student_id}.")
        else:
            print(f"Student {student_id} deleted successfully.")

    except psycopg.Error as error:
        print(f"Error deleting student: {error}")

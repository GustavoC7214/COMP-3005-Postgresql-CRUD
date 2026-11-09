# COMP 3005 — PostgreSQL CRUD Application

A Python command-line application that connects to a PostgreSQL database to perform Create, Read, Update, and Delete (CRUD) operations on student records.

## Technologies

- Python 3
- PostgreSQL
- psycopg 3
- SQL

## Project Structure

```text
COMP-3005-Postgresql-CRUD/
├── app/
│   ├── database.py
│   └── main.py
├── database/
│   ├── schema.sql
│   └── seed.sql
├── .gitignore
├── README.md
└── requirements.txt
```

## Prerequisites

- Python 3.10 or later
- PostgreSQL installed and running
- pip
- pgAdmin (recommended for database inspection)

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/GustavoC7214/COMP-3005-Postgresql-CRUD.git
cd COMP-3005-Postgresql-CRUD
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Create the PostgreSQL database

Ensure PostgreSQL is running, then execute:

```bash
createdb student_db
```

### 5. Create the table

```bash
psql -d student_db -f database/schema.sql
```

### 6. Insert the initial data

```bash
psql -d student_db -f database/seed.sql
```

Run the seed script only once to avoid duplicate-email errors.

### 7. Configure the database connection

The application uses the following defaults:

- Database: `student_db`
- User: Current operating system username
- Host: `localhost`
- Port: `5432`

If your PostgreSQL configuration differs, set environment variables before running the application.

Example:

```bash
export DB_NAME=student_db
export DB_USER=postgres
export DB_HOST=localhost
export DB_PORT=5432
export DB_PASSWORD=your_password
```

Replace the example username and password with your actual PostgreSQL credentials.

### 8. Run the application

From the project root:

```bash
python -m app.main
```

## Application Functions

**1. getAllStudents()**

Retrieves and displays every student record, ordered by student ID.

**2. addStudent(first_name, last_name, email, enrollment_date)**

Inserts a student into the database. The student ID is generated automatically.

**3. updateStudentEmail(student_id, new_email)**

Updates the email address of the student identified by the supplied ID.

**4. deleteStudent(student_id)**

Deletes a student record using its ID.

## Database Schema

The `students` table contains:

| Column | Type | Constraints |
|---|---|---|
| student_id | INTEGER | Primary Key, Identity |
| first_name | TEXT | NOT NULL |
| last_name | TEXT | NOT NULL |
| email | TEXT | NOT NULL, UNIQUE |
| enrollment_date | DATE | Optional |

## Initial Data

| ID | First Name | Last Name | Email | Enrollment Date |
|---|---|---|---|---|
| 1 | John | Doe | john.doe@example.com | 2023-09-01 |
| 2 | Jane | Smith | jane.smith@example.com | 2023-09-01 |
| 3 | Jim | Beam | jim.beam@example.com | 2023-09-02 |

## Error Handling

The application handles common database and input errors, including duplicate email addresses, invalid dates, nonexistent student IDs, and invalid menu selections.

SQL queries use parameterized statements to prevent SQL injection.

## Demonstration Video

Video link: **To be added after recording and uploading.**

The demonstration covers PostgreSQL database setup, the four CRUD functions, and verification of database changes using pgAdmin.

## Author

Gustavo Chaves

COMP 3005 — Database Management Systems


-- COMP 3005 - PostgreSQL CRUD Application
-- Inserts the three initial students required by the assignment.
-- Run this script once after creating the table.

INSERT INTO students (
    first_name,
    last_name,
    email,
    enrollment_date
)
VALUES
    ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
    ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
    ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');

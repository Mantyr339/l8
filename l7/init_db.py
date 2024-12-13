import psycopg2

# Параметри підключення
connection = psycopg2.connect(
    host="localhost",
    database="hr_database",
    user="hr_user",
    password="hr_password",
    port="5432"
)
cursor = connection.cursor()

# Створення таблиць
cursor.execute("""
CREATE TABLE IF NOT EXISTS Departments (
    department_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    room_number INT CHECK (room_number BETWEEN 701 AND 710)
);

CREATE TABLE IF NOT EXISTS Positions (
    position_id SERIAL PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    salary NUMERIC NOT NULL,
    bonus_percentage NUMERIC CHECK (bonus_percentage BETWEEN 0 AND 100)
);

CREATE TABLE IF NOT EXISTS Employees (
    employee_id SERIAL PRIMARY KEY,
    last_name VARCHAR(50) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    middle_name VARCHAR(50),
    address TEXT,
    phone VARCHAR(15) NOT NULL,
    education VARCHAR(50) CHECK (education IN ('Спеціальна', 'Середня', 'Вища')),
    department_id INT REFERENCES Departments(department_id) ON DELETE CASCADE,
    position_id INT REFERENCES Positions(position_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Projects (
    project_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    deadline DATE NOT NULL,
    budget NUMERIC NOT NULL
);

CREATE TABLE IF NOT EXISTS ProjectExecution (
    execution_id SERIAL PRIMARY KEY,
    project_id INT REFERENCES Projects(project_id) ON DELETE CASCADE,
    department_id INT REFERENCES Departments(department_id) ON DELETE CASCADE,
    start_date DATE NOT NULL
);
""")

connection.commit()
print("Tables created successfully.")
cursor.close()
connection.close()

import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="hr_database",
    user="hr_user",
    password="hr_password",
    port="5432"
)
cursor = connection.cursor()

# Заповнення даних
cursor.execute("""INSERT INTO Departments (name, phone, room_number)
VALUES
('Програмування', '0501234567', 701),
('Дизайн', '0509876543', 702),
('ІТ', '0505554444', 703);
""")

cursor.execute("""INSERT INTO Positions (title, salary, bonus_percentage)
VALUES
('Інженер', 2500, 10),
('Редактор', 2000, 8),
('Програміст', 3000, 12);
""")

cursor.execute("""
INSERT INTO Employees (last_name, first_name, middle_name, address, phone, education, department_id, position_id)
VALUES
('Іваненко', 'Іван', 'Іванович', 'Київ, вул. Хрещатик, 10', '0501234567', 'Вища', 1, 3),
('Іванов', 'Никола', 'Іванович', 'Київ', '123-111-1111', 'Вища', 1, 3),
('Петренко', 'Петро', 'Петрович', 'Львів', '123-222-2222', 'Середня', 2, 2),
('Сидоренко', 'Сидір', 'Сидорович', 'Одеса', '123-333-3333', 'Спеціальна', 3, 1);
""")

cursor.execute("""
INSERT INTO Projects (name, deadline, budget)
VALUES
('Проект A', '2024-12-31', 50000),
('Проект B', '2025-06-30', 75000);
""")

cursor.execute("""
INSERT INTO ProjectExecution (project_id, department_id, start_date)
VALUES
(1, 1, '2024-01-15'),
(2, 2, '2024-02-01');
""")

connection.commit()
print("Data inserted successfully.")
cursor.close()
connection.close()

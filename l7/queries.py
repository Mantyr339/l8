import psycopg2
from prettytable import PrettyTable

# Підключення до бази даних
connection = psycopg2.connect(
    host="localhost",
    database="hr_database",
    user="hr_user",
    password="hr_password",
    port="5432"
)
cursor = connection.cursor()

# Запит 1: Робітники з окладом > 2000, відсортовані за прізвищем
cursor.execute("""
SELECT last_name, first_name, salary
FROM Employees
JOIN Positions ON Employees.position_id = Positions.position_id
WHERE salary > 1999
ORDER BY last_name;
""")
rows = cursor.fetchall()
table = PrettyTable(["Прізвище", "Ім'я", "Оклад"])
for row in rows:
    table.add_row(row)
print("Запит 1: Робітники з окладом > 2000")
print(table)

# Запит 2: Середня зарплатня в кожному відділі
cursor.execute("""
SELECT Departments.name, AVG(salary) AS average_salary
FROM Employees
JOIN Positions ON Employees.position_id = Positions.position_id
JOIN Departments ON Employees.department_id = Departments.department_id
GROUP BY Departments.name;
""")
rows = cursor.fetchall()
table = PrettyTable(["Назва відділу", "Середня зарплатня"])
for row in rows:
    table.add_row(row)
print("\nЗапит 2: Середня зарплатня в кожному відділі")
print(table)

# Запит 3: Всі проекти, які виконуються у вказаному відділі
department_id = 1  # Задайте ID відділу, що цікавить
cursor.execute("""
SELECT Projects.project_id, Projects.name, Projects.budget
FROM Projects
JOIN ProjectExecution ON Projects.project_id = ProjectExecution.project_id
WHERE ProjectExecution.department_id = %s;
""", (department_id,))
rows = cursor.fetchall()
table = PrettyTable(["ID Проекту", "Назва проекту", "Бюджет"])
for row in rows:
    table.add_row(row)
print(f"\nЗапит 3: Проекти, які виконуються у відділі з ID {department_id}")
print(table)

# Запит 4: Кількість працівників у кожному відділі
cursor.execute("""
SELECT Departments.name, COUNT(*) AS employee_count
FROM Employees
JOIN Departments ON Employees.department_id = Departments.department_id
GROUP BY Departments.name;
""")
rows = cursor.fetchall()
table = PrettyTable(["Назва відділу", "Кількість працівників"])
for row in rows:
    table.add_row(row)
print("\nЗапит 4: Кількість працівників у кожному відділі")
print(table)

# Запит 5: Розмір премії для кожного працівника
cursor.execute("""
SELECT last_name, first_name, salary, (salary * bonus_percentage / 100) AS bonus
FROM Employees
JOIN Positions ON Employees.position_id = Positions.position_id;
""")
rows = cursor.fetchall()
table = PrettyTable(["Прізвище", "Ім'я", "Оклад", "Премія"])
for row in rows:
    table.add_row(row)
print("\nЗапит 5: Розмір премії для кожного працівника")
print(table)

# Запит 6: Кількість працівників із різними рівнями освіти в кожному відділі
cursor.execute("""
SELECT 
    Departments.name AS department_name, 
    Employees.education AS education_level, 
    COUNT(*) AS count
FROM Employees
JOIN Departments ON Employees.department_id = Departments.department_id
GROUP BY Departments.name, Employees.education;
""")
rows = cursor.fetchall()

table = PrettyTable(["Назва відділу", "Рівень освіти", "Кількість"])

for row in rows:
    table.add_row(row)

print("\nЗапит 6: Кількість працівників із різними рівнями освіти у відділах")
print(table)

# Закриття курсора і з'єднання
cursor.close()
connection.close()

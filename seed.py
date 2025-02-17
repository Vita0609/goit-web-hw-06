import sqlite3
from faker import Faker
import random

fake = Faker()

conn = sqlite3.connect("university.db")
cursor = conn.cursor()

# Проверяем, есть ли таблицы
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
existing_tables = [table[0] for table in cursor.fetchall()]

if (
    "groups" not in existing_tables
    or "teachers" not in existing_tables
    or "subjects" not in existing_tables
    or "students" not in existing_tables
    or "grades" not in existing_tables
):
    print(
        "Ошибка: одна или несколько таблиц отсутствуют. Проверьте структуру базы данных!"
    )
    conn.close()
    exit()

# Добавляем группы
groups = ["Группа A", "Группа B", "Группа C"]
for group in groups:
    cursor.execute("INSERT INTO groups (name) VALUES (?)", (group,))

# Добавляем преподавателей
teachers = [fake.name() for _ in range(4)]
for teacher in teachers:
    cursor.execute("INSERT INTO teachers (full_name) VALUES (?)", (teacher,))

# Добавляем предметы
subjects = ["Математика", "Физика", "Программирование", "Философия", "Английский"]
teacher_ids = [row[0] for row in cursor.execute("SELECT id FROM teachers").fetchall()]
for subject in subjects:
    teacher_id = random.choice(teacher_ids)
    cursor.execute(
        "INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (subject, teacher_id)
    )

# Добавляем студентов
group_ids = [row[0] for row in cursor.execute("SELECT id FROM groups").fetchall()]
students = [fake.name() for _ in range(40)]
for student in students:
    group_id = random.choice(group_ids)
    cursor.execute(
        "INSERT INTO students (full_name, group_id) VALUES (?, ?)", (student, group_id)
    )

# Добавляем оценки
student_ids = [row[0] for row in cursor.execute("SELECT id FROM students").fetchall()]
subject_ids = [row[0] for row in cursor.execute("SELECT id FROM subjects").fetchall()]
for student_id in student_ids:
    for subject_id in subject_ids:
        for _ in range(random.randint(5, 20)):  # Генерируем до 20 оценок
            grade = random.randint(50, 100)
            date_received = fake.date_this_decade()
            cursor.execute(
                "INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?)",
                (student_id, subject_id, grade, date_received),
            )

conn.commit()
conn.close()

print("База данных заполнена случайными данными!")

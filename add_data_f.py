from datetime import datetime, date, timedelta
from faker import Faker
from random import randint, choice, random
import sqlite3
from sqlite3 import connect, Error 
# import pprint

fake = Faker('uk_UA')

def generate_group_name():
    letters = [choice('АБВГДЕЄЖЗИІКЛМНОПРСТУФХЦЧШЩЮЯ') for _ in range(3)]
    group_name = ''.join(letters) + '-' + str(randint(0, 9))
    return group_name

groups = [generate_group_name() for _ in range(3)] # Генеруємо назви груп
subjects = [fake.job() for _ in range(10)] # Генеруємо назви умовних предметів
teachers = []
students = []

NUMBER_TEACHERS = 5
NUMBER_STUDENTS = 50

connect = sqlite3.connect("hw.db")
cur = connect.cursor()

def seed_teachers():
    teachers = [fake.name() for _ in range(NUMBER_TEACHERS)]
    sql = "INSERT INTO teachers(name) VALUES(?);" #future replace on run scripts from folder
    cur.executemany(sql,zip(teachers,))

def seed_subject():
    sql = "INSERT INTO subjects(subject_name, teacher_id) VALUES(?, ?);"
    for subject in subjects:
        try:
            cur.execute(sql, (subject, randint(1, NUMBER_TEACHERS)))
        except sqlite3.IntegrityError as e:
                continue
    # для релізу коли предмети заповнюються не фейкером    
    # cur.executemany(sql,zip(subjects, iter(randint(1, NUMBER_TEACHERS)
    #                                        for _ in range(len(subjects)) )))

def seed_groups():
    sql = "INSERT INTO groups(group_name) VALUES(?);" #future replace on run scripts from folder
    cur.executemany(sql,zip(groups,))

def seed_students():
    students = [fake.name() for _ in range(NUMBER_STUDENTS)]
    sql = "INSERT INTO students(name, group_id) VALUES(?,?);" #future replace on run scripts from folder
    cur.executemany(sql,zip(students, iter(randint(1, len(groups))
                                           for _ in range(len(students)) )))

def seed_grades():
    start_date = datetime.strptime("2022-09-01","%Y-%m-%d")
    # end_date = datetime.strptime("2024-06-30","%Y-%m-%d")
    end_date = datetime.today()
    sql = "INSERT INTO grades(subject_id, student_id, grade, grade_date) VALUES(?, ?, ?, ?);"

    def get_list_date(start: date, end: date):
        result = []
        current_date = start
        while current_date <= end:
            if current_date.isoweekday() < 6:
                result.append (current_date)
            current_date += timedelta(1)
        return result
        
    list_dates = get_list_date(start_date, end_date)
    grades = []
    for day in list_dates:
        random_subject = randint(1, len(subjects))
        random_student = [randint(1, NUMBER_STUDENTS) for _ in range(5)]
        for student in random_student:
            grades.append((random_subject, student, randint (10,100), day.date()))
    cur.executemany(sql, grades)




if __name__ == '__main__':
    error = Exception
    try:
        seed_teachers()
        seed_subject()
        seed_groups()
        seed_students()
        seed_grades()
        connect.commit()
    except sqlite3.Error as error:
        print(error)
    finally:
        connect.close





# second.py



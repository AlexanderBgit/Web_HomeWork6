DROP TABLE IF EXISTS groups;
CREATE TABLE [groups] (
    group_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    group_name VARCHAR(50)
);

-- students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name VARCHAR(255),
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups (group_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- teachers
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    teacher_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);

-- subjects
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
    subject_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    subject_name VARCHAR(255) UNIQUE NOT NULL,
    teacher_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (teacher_id) REFERENCES teachers (teacher_id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

-- grades
DROP TABLE IF EXISTS grades;
CREATE TABLE grades (
    grade_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    student_id INTEGER,
    subject_id INTEGER,
    grade INTEGER,
    grade_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students (student_id)
      ON DELETE CASCADE
      ON UPDATE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects (subject_id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

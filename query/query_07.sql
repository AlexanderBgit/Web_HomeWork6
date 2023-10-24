SELECT s.name, g.grade, g.grade_date AS lesson_date
FROM students s
JOIN grades g ON s.student_id = g.student_id
JOIN subjects sub ON g.subject_id = sub.subject_id
WHERE s.group_id = 2 AND sub.subject_id = 5
ORDER BY s.name;

SELECT  ROUND(AVG(g.grade), 1) AS avg_grade
FROM    grades g
JOIN    subjects sub ON g.subject_id = sub.subject_id
JOIN    students s ON g.student_id = s.student_id
WHERE   sub.teacher_id = 4 AND s.student_id = 10;



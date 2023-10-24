SELECT sub.subject_name
FROM subjects sub
JOIN grades g ON sub.subject_id = g.subject_id
WHERE g.student_id = 10 AND sub.teacher_id = 4
GROUP BY sub.subject_name;

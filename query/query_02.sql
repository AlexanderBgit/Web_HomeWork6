SELECT s.name, ROUND(AVG(g.grade),2) AS avg_grade
FROM students s
JOIN grades g ON s.student_id = g.student_id
JOIN subjects sub ON g.subject_id = sub.subject_id
WHERE sub.subject_id = 3
GROUP BY s.name
ORDER BY avg_grade DESC
LIMIT 1;

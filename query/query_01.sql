SELECT s.name, ROUND(AVG(g.grade),2) AS avg_grade
FROM students s
JOIN grades g ON s.student_id = g.student_id
GROUP BY s.name
ORDER BY avg_grade DESC
LIMIT 5;

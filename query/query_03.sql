SELECT g.group_name, ROUND(AVG(gg.grade),1) AS avg_grade
FROM groups g
JOIN students s ON g.group_id = s.group_id
JOIN grades gg ON s.student_id = gg.student_id
JOIN subjects sub ON gg.subject_id = sub.subject_id
WHERE sub.subject_id = 2
GROUP BY g.group_name;

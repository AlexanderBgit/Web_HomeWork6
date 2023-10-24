-- середній бал по всім предметам одного викладача

-- SELECT ROUND(AVG(g.grade),1) AS avg_grade
-- FROM grades g
-- JOIN subjects sub ON g.subject_id = sub.subject_id
-- WHERE sub.teacher_id = 4;


-- середній бал по кожному з предметів викладача
SELECT sub.subject_name, ROUND(AVG(g.grade), 1) AS avg_grade
FROM grades g
JOIN subjects sub ON g.subject_id = sub.subject_id
WHERE sub.teacher_id = 4
GROUP BY sub.subject_name;

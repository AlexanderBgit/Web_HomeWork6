SELECT 	s.name, g.grade, g.grade_date AS last_lesson_date
FROM 	students s
JOIN 	grades g ON s.student_id = g.student_id
JOIN 	subjects sub ON g.subject_id = sub.subject_id
WHERE 	s.group_id = 1 AND sub.subject_id = 8
      AND g.grade_date = (SELECT MAX(grade_date) 
	  FROM grades WHERE subject_id = sub.subject_id);

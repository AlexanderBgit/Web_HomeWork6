SELECT grade AS mode
FROM grades
GROUP BY grade
ORDER BY COUNT(*) DESC
LIMIT 1;

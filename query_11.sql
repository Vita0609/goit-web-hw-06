SELECT students.full_name AS student, teachers.full_name AS teacher, AVG(grades.grade) AS avg_grade
FROM grades
JOIN students ON grades.student_id = students.id
JOIN subjects ON grades.subject_id = subjects.id
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE students.full_name = 'Igor Petrov' AND teachers.full_name = 'Anna Ivanova'
GROUP BY students.id, teachers.id;



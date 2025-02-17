SELECT teachers.full_name, AVG(grades.grade) AS avg_grade
FROM subjects
JOIN teachers ON subjects.teacher_id = teachers.id
JOIN grades ON subjects.id = grades.subject_id
WHERE teachers.id = 1
GROUP BY teachers.id;


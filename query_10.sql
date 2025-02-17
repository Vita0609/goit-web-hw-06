SELECT DISTINCT subjects.name
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
WHERE grades.student_id = 1 AND subjects.teacher_id = 1;


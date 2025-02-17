SELECT students.full_name, grades.grade, grades.date_received
FROM students
JOIN grades ON students.id = grades.student_id
WHERE students.group_id = 1 AND grades.subject_id = 1;


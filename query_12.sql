SELECT students.full_name, grades.grade, grades.date_received
FROM grades
JOIN students ON grades.student_id = students.id
JOIN subjects ON grades.subject_id = subjects.id
WHERE students.group_id = (
    SELECT id FROM groups WHERE name = 'Groupe A'
)
AND grades.subject_id = (
    SELECT id FROM subjects WHERE name = 'Match'
)
AND grades.date_received = (
    SELECT MAX(date_received)
    FROM grades
    WHERE grades.subject_id = (
        SELECT id FROM subjects WHERE name = 'Match'
    )
);


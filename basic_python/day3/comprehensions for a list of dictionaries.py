students = [
    {"name":"Veenus","age":30,"grade":"A"},
    {"name":"Krishna","age":25,"grade":"A+"},
    {"name":"Ritu","age":18,"grade":"A"}
]
name=[student['name'] for student in students]
grades_A_stud = [student['name'] for student in students if student['grade'] == 'A']
print("Names of all students:", name)
print("Students with grade 'A':", grades_A_stud)
name_age = [(student['name'], student['age']) for student in students]
print("Names and Ages of students: ", name_age)
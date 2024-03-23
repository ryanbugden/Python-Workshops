student_names = ["Amanda", "Javier", "JJ", "Hui", "Mina"]
absent_students = ["Ruby", "Renald"]
print(student_names)
how_many_students_here = len(student_names)
how_many_absent_students = len(absent_students)

last_student = student_names[-1]
print("Last student in list?", last_student)

print(last_student.upper())

print(how_many_students_here, how_many_absent_students)
print(how_many_students_here + how_many_absent_students)

all_students = student_names + absent_students
print(all_students)
print(len(all_students))



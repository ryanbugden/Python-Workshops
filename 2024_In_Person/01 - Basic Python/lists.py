# Make two separate lists
student_names   = ["Amanda", "Javier", "JJ", "Hui", "Mina"]
absent_students = ["Ruby", "Renald"]
print(student_names)

# Get the last student in the list by the index -1
last_student = student_names[-1]
print("Last student in list?", last_student)
print(last_student.upper())

# Store the lengths of those lists in variables
how_many_students_here = len(student_names)
how_many_absent_students = len(absent_students)
# Print the two separate lengths 
print(how_many_students_here, how_many_absent_students)
print(how_many_students_here + how_many_absent_students)

# Make a new combined list (all students together)
all_students = student_names + absent_students
# Print the list
print(all_students)
# Print how many students there are altogether
print(len(all_students))



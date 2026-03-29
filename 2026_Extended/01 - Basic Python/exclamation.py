# Make a list of students
my_students = ["Francine", "Andrew", "Rebecca", "Wei Wei"]
# Print the first student
print(my_students[0])

# Make an empty list to populate later
exclamatory_students = []
# Loop through every student name in the list
for student_name in my_students:
    # If the first letter of the student’s name is F, add the name to the list of exclamatory_students, and add "!!!"
    if student_name[0] != "F":
        exclamatory_students.append(student_name + "!!!")
        
# Print out our new list that we just built, on the fly
print(exclamatory_students)

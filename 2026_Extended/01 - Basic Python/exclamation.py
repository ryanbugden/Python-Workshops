my_students = ["Francine", "Andrew", "Rebecca", "Wei Wei"]
print(my_students[0])

exclamatory_students = []
for student_name in my_students:
    # print(student_name + " is cool.")
    print(student_name[0])
    if student_name[0] != "F":
        exclamatory_students.append(student_name + "!!!")
    
print(exclamatory_students)

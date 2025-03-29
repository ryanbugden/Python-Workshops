from random import randint

# Start with a list of names
students = ['Elisabetta', 'Jisung', 'Jesse', 'Christine']

# Make empty dictionary
how_many_styles_per_student = {}
# Loop through student names
for student_name in students:    
    # For each student name, assign a random number of styles
    random_number = randint(0, 400)
    # Add it to the dictionary
    how_many_styles_per_student[student_name] = random_number

# Look at final dictionary
print(how_many_styles_per_student)
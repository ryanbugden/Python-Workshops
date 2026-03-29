from random import randint

# Make two different lists
four_students = ['Elisabetta', 'Jisung', 'Jesse', 'Christine']
other_four = ['Rocco', 'Kelly', 'Carsi', 'Paige']

# Define a function
def assign_random_numbers(list_of_students):
    # Make empty dictionary
    how_many_styles_per_student = {}
    # Loop through student names
    for student_name in list_of_students:    
        # For each student name, assign a random number of styles
        random_number = randint(0, 400)
        # Add it to the dictionary
        how_many_styles_per_student[student_name] = random_number
    return how_many_styles_per_student
    
# Use the function on each of the lists
print(assign_random_numbers(four_students))
print(assign_random_numbers(other_four))
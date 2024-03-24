from random import choice

# Store a list of students’ names
student_names = ["Amanda", "Javier", "JJ", "Hui", "Mina"]
# Choose the best student at random, and store it in a variable
best_student = choice(student_names)
# Print the selection
print(best_student)

# Make everything lowercase, and print conditional reactions
best_student = best_student.lower()
if best_student == "mina":
    print("Yay!")
elif best_student == "amanda":
    print("Okay cool.")
elif best_student == "javier":
    print("What's up?")
elif best_student == "hui":
    print("Hey!")
elif best_student == "jj":
    print("Alright.")
else:
    print("Oh no.")


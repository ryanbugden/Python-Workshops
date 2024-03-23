from random import choice

student_names = ["Amanda", "Javier", "JJ", "Hui", "Mina"]
best_student = choice(student_names)

print(best_student)
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


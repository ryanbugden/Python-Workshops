from random import choice

student_names = ["Amanda", "Javier", "JJ", "Hui", "Mina"]
who_to_find = "JJ"

for name in student_names:
    if name == who_to_find:
        print(f"Found {who_to_find}!")
        break
    else:
        print(f"Not {who_to_find}. This is {name}.")


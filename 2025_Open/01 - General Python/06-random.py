from random import randint

cool_students = ["Léna", "Ben", "Fabian", "Yi", "Kai", "Chris"] * 100

# Generate a random integer between 0 and the length of that list minus 1
random_number = randint(0, len(cool_students) - 1)
print(random_number)
# Show who was picked
print(cool_students[random_number])

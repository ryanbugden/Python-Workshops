           # This is a tuple
students = ("Katie", "Francine", "Rochell", "Andrew")

# Loop through every name in the tuple of students
for name in students:
    # Print each name
    print(name)
    # Once at the name, loop through each letter in the name...
    for character in name:
        # ... and print it
        print(character)
from random import choice

# Make a list
student_names = ["Amanda", "Javier", "JJ", "Hui", "Mina"]
# Choose a name to find in the list
who_to_find = "JJ"

# Loop through each name in the list
for name in student_names:
    # If it's a hit, tell me.
    if name == who_to_find:
        print(f"Found {who_to_find}!")
        # And stop looping
        break
    # If it's not a hit yet, tell me.
    else:
        print(f"Not {who_to_find}. This is {name}.")


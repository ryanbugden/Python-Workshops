# Make a string, and choose two random letters
letters = "wertyui?"
first_choice = choice(letters)
second_choice = choice(letters)

# Make a new list full og 10 new random choices
letter_choices = []
for i in range(10):
    letter_choices.append(choice(letters))
# Print it
print(letter_choices)
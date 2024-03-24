letters = "wertyui?"
first_choice = choice(letters)
second_choice = choice(letters)

letter_choices = []
for i in range(10):
    letter_choices.append(choice(letters))
    
print(letter_choices)
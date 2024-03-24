# Make a list
student_names = ["Amanda", "Javier", "JJ", "Hui", "Mina"]
student_names += ["Renald"]
# Expand the list by 100 times
student_names *= 100
print(student_names)

# Loop Through each name, assigning a random DIY variable
i = 0
# Start counting
for pizza_time in student_names:
    print(i, pizza_time)
    i += 1
    
# Print each name, but in all-caps
for pizza_time in student_names:
    print(pizza_time.upper())


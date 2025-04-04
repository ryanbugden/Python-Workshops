# Lists!
cool_students = ["Léna", "Ben", "Fabian", "Yi", "Kai", "Chris"]
# cool_students.append("Ryan")
# cool_students.remove("Ryan")
print(cool_students)
# Print the laste student’s name
print(cool_students[-1])
# Print up until the 4th student
print(cool_students[:3])
# Print the 2nd up until the 4th student
print(cool_students[1:3])
print("---")


# Dictionaries!
favorite_colors = {
    # Key     # Value
    "Fabian": "Blue", 
    "Ben":    ["Chartreuse", "Violet"], 
    "Léna":   "Puce",
    }
print(favorite_colors)
# Print Ben’s favorite color
print(favorite_colors["Ben"])
# Set Ryan’s favorite color as you add him to the dictionary
favorite_colors["Ryan"] = "Green"
print(favorite_colors)
# Print Ryan’s favorite color
print(favorite_colors["Ryan"])
print("---")


# Tuples! Like lists, but less flexible, more static.
cool_students = ("Léna", "Ben", "Fabian", "Yi", "Kai", "Chris")
print(cool_students)
point_coordinates = (0, 20)
print(point_coordinates)
cool_color = (1,0,0)
print(cool_color)

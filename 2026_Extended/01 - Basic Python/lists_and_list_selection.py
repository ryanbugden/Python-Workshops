students = ["Dorian", "Clara", "Katie", "Rochell"]

print(students)
# Get the first student
print(students[0])
# Get the last student
print(students[-1])
# Kick Dorian out
students.remove("Dorian")
# Add Wei Wei to the end
students.append("Wei Wei")
# Add Rebecca to the beginning
students.insert(0, "Rebecca")
# Check the list again
print(students)
# Check where Katie is in the list
print(students.index("Katie"))
# Lengthen the list by 100 times
print(students * 100)
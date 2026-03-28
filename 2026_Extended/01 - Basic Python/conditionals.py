# Make a list full of student names
students_present = ["Jasmin", "Shiqing"]

# Check to see if Leah is present
if "Leah" in students_present:
    print("Leah is here!")
# If not, check to see if Antonio Banderas is present
elif "Antonio Banderas" in students_present:
    print("Leah is not here, but Antonio Banderas is!!")
# If not, check to see if Sergio is present
elif "Sergio" in students_present:
    print("Leah is not here, Antonio Banderas is not here. But Sergio is!!")
# Here’s the catch-all condition
else:
    print("Neither Sergio nor Leah nor Antonio are here! Oh no!")
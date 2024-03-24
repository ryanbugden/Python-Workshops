# Store some data in a dictionary
student_stuff = {
            "Javier": ["Laptop", "Phone", "Sunglasses"], 
            "Amanda": ["Bottle", "Laptop"]
            }

# Loop through the dictionary
for student_name, possessions in student_stuff.items():
    # Give each person 100 dollars by adding it to their list
    student_stuff[student_name] += ["100 dollars"]
    
# See the updated dictionary
print(student_stuff)
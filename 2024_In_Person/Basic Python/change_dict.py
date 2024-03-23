student_stuff = {
            "Javier": ["Laptop", "Phone", "Sunglasses"], 
            "Amanda": ["Bottle", "Laptop"]
            }

for student_name, possessions in student_stuff.items():
    # print(student_name, possessions)
    student_stuff[student_name] += ["100 dollars"]
    
print(student_stuff)
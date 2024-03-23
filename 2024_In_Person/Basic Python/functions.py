
def find_person(which_student, list_of_student_names):
    found = False
    for name in list_of_student_names:
        if name == which_student:
            print("Found!")
            found = True
    if found == False:
        print("This person is not here.")
        

student_names = ["Amanda", "Javier", "JJ", "Hui", "Mina"]
celebrities = ["Angelina Jolie", "Brad Pitt", "Samuel L Jackson"]

find_person("Brad Pitt", student_names)
find_person("Brad Pitt", celebrities)
find_person("Mina", celebrities)
find_person("Mina", student_names)


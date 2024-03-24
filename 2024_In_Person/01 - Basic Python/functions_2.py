from random import choice

# Make a function to print a string 100 times
def repeat(my_string):
    my_string_with_space = choice(my_string).upper() + " "
    print(my_string_with_space * 100)
    
repeat("hello")
repeat("this")
repeat("is Python")


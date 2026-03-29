from random import randint

# Make a function that says Hi between 1 and 100 times (randomly)
def say_hi_alot():
    print("Hi " * randint(1, 100))    

# Run the function
say_hi_alot()
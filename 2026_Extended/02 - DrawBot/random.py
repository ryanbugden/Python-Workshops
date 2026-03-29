# This is a script about random functions

# random() gives you a random FLOAT between 0 and 1
print(random() * 200)

# randint() gives you a random integer between 2 given inputs
print(randint(-100, 0))
# rect(randint(0, 1000), randint(0, 1000), randint(0, 1000), randint(0, 1000))
one_random_number = randint(0, 1000)
print(one_random_number)
rect(one_random_number, one_random_number, one_random_number, one_random_number)

# choice() gives you a random choice from a given dataset
my_list = ["Cup", "Plate", "Knife"]
print(choice(my_list))


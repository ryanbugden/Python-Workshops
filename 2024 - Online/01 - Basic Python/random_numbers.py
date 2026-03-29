# Import random from outside of DrawBot
from random import random

# Get random number from 0 to 1
my_random_number = random()
print(my_random_number)
# Make it into a random number from 0 to 1000
print(int(my_random_number*1000))
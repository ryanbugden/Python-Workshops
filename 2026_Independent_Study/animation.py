from random import random

# Establishing our variables
my_width  = 1000
my_height = 4000
my_margin = 40

# For loop, looping through each number
for frame in range(10):
    print("I am making frame number:", frame)
    # Setting up the page
    newPage(my_width, my_height)

    # Drawing stuff
    fill(random(), random(), random(), 1)
    rect(my_margin, my_margin, my_width - my_margin*2, my_height - my_margin*2)

    fill(random(), random(), random(), 1)
    oval(my_margin, my_margin, my_width - my_margin*2, my_height - my_margin*2)

    stroke(random(), random(), random(), 1)
    strokeWidth(25)
    line((my_margin, my_margin), (my_width - my_margin, my_height - my_margin))
    print("I drew stuff in it!\n")

# Save all frames as a gif
saveImage("~/Desktop/animation.gif")
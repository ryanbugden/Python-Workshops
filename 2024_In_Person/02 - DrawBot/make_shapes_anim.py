from random import random

my_colors = [
            (1,0,0),
            (1,1,0),
            (1,0,1),
            (0,0,1),
            (0,1,0),
            ]

# Define a function to make a target shape
def make_target(my_radius):
    # Store the big radius
    starting_radius = my_radius
    for number in range(10):
        print("Drawing an oval")
        fill(*choice(my_colors))
        oval(my_width/2 - my_radius, my_height/2 - my_radius, my_radius*2, my_radius*2)
        # Each time, reduce the size of the circle by a tenth of the starting radius.
        my_radius -= starting_radius / 10

my_width = 1920    
my_height = 1080

overall_target_radius = 10
for page in range(20):
    # Make the page
    newPage(my_width, my_height)
    frameDuration(1/60)
    # Draw the red background
    fill(1, 0, 0, 1)
    rect(0, 0, my_width, my_height)
    # Make the target
    make_target(overall_target_radius)
    overall_target_radius += 30
    
# Export an animated gif
saveImage("target_stuff.gif")


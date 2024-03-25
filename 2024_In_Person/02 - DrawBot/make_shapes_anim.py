from random import random

# Set some variables for page size
my_width = 1920    
my_height = 1080

# Make list of nice colors
my_colors = [
            (1,0,0),
            (1,1,0),
            (1,0,1),
            (0,0,1),
            (0,1,0),
            ]

# Define a function that makes a target shape
def make_target(radius):
    # Store the big radius
    new_radius = radius
    for number in range(10):
        print("Drawing an oval")
        fill(*choice(my_colors))
        oval(my_width/2 - new_radius, my_height/2 - new_radius, new_radius*2, new_radius*2)
        # Each time, reduce the size of the circle by a tenth of the starting radius.
        new_radius -= radius / 10

# Loop through 20 pages, starting with a radius of 10
outside_radius = 10
for page in range(20):
    # Make the page
    newPage(my_width, my_height)
    # Set how long this frame stays on in the GIF animation
    frameDuration(1/60)
    # Draw the red background
    fill(1, 0, 0, 1)
    rect(0, 0, my_width, my_height)
    # Make the target, using our function above
    make_target(outside_radius)
    # For each new page, increase the radius by 30
    outside_radius += 30
    
# Export an animated gif
saveImage("_output/target_stuff.gif")


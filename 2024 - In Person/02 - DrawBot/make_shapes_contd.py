from random import random

# Decide upon a radius and amount of circles in your target
outside_radius = 500
total_circles = 100

# Make a page
my_width = 1920    
my_height = 1080
newPage(my_width, my_height)

# Draw a random color background
fill(random(), random(), random())
rect(0, 0, my_width, my_height)

# Your radius will change, but start with outside radius you decided up there.
my_radius = outside_radius
for circle_number in range(total_circles):
    # Tell me what circle you're on
    print(f"Drawing circle #{circle_number + 1}")
    # Choose a random color for the circle
    fill(random(), random(), random())
    # Draw the circle, centered on the page
    oval(my_width/2 - my_radius, my_height/2 - my_radius, my_radius*2, my_radius*2)
    # Decrease the radius for the next circle
    my_radius -= outside_radius / total_circles

saveImage("_output/cool_target.png")
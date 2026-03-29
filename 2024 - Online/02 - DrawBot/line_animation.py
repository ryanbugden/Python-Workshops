from random import randint

# Set width and height
my_width  = 1200
my_height = 1200

# Choose frames for second
frames_per_second = 30

# Make all the pages
for anything in range(50):
    # Start a new page
    newPage(my_width, my_height)
    # Set frame duration
    frameDuration(1/frames_per_second)
    stroke(0)
    # Choose a random stroke width
    strokeWidth(randint(4, 50))
    # Draw a line
    line((100, 100), (900, 900))
    print("Adding a page to a GIF")

# Save all the pages in one GIF
saveImage('_output/line_animation.gif')
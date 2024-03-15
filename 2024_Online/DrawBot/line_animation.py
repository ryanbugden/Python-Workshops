from random import randint

# Set width and height
my_width  = 1200
my_height = 1200

frames_per_second = 30

# Make all the pages
for anything in range(50):
    # Start a new page
    newPage(my_width, my_height)
    frameDuration(1/frames_per_second)
    stroke(0)
    strokeWidth(randint(4, 50))
    line((10, 10), (10, 10)), (900, 900))
    print("Adding a page to a GIF")

# Save all the pages in one document
saveImage('~/Desktop/line_animation.gif')
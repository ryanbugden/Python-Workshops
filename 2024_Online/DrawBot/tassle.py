from random import randint, random

# Choose width and height to use later
my_width  = 1000
my_height = 1000

# Choose a number of pages to make for your GIF
num_pages = 40

# Iterate through every page number from 0 to 39 (40-count)
for page_number in range(num_pages):
    # Make a new page
    newPage(my_width, my_height)
    # Set fill to black
    fill(0)
    # Make a background shape
    rect(0, 0, my_width, my_height)
    
    # Choose a color that changes slightly for each page
    color_value = page_number / num_pages
    
    # Build a list of 50 random start points for this line
    start_points = []
    for i in range(50):
        new_coord = (randint(100, 400), randint(100, 400))
        start_points.append(new_coord)

    # Loop through all of the start points, not changing the endpoint
    for pt in start_points:
        stroke(color_value, random(), color_value)
        strokeWidth(10)
        # Draw a line from each start point to (900, 900)
        line(pt, (900, 900))
        
# Export all the pages you made as a multi-frame GIF
saveImage("_output/tassle.gif")
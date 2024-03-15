from random import randint, random

# Set width and height
my_width  = 1000
my_height = 1000

num_pages = 40

for page_number in range(num_pages):
    # Start a new page
    newPage(my_width, my_height)
    fill(0)
    rect(0, 0, my_width, my_height)
    
    color_value = page_number / num_pages
    
    start_points = []
    for i in range(50):
        new_coord = (randint(100, 400), randint(100, 400))
        start_points.append(new_coord)

    for pt in start_points:
        stroke(color_value, random(), color_value)
        strokeWidth(10)
        line(pt, (900, 900))
        
saveImage("~/Desktop/tassle.gif")
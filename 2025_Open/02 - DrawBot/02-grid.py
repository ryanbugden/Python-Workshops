from random import random


# Make a function that makes a couple of shapes, given a position and size
def make_custom_shapes(x, y, w, h):
    # Fill a rectangle with a random color
    fill(random(), random(), random())
    rect(x, y, w, h)
    # Fill a smaller inset oval with a different random color
    fill(random(), random(), random())
    oval(x + w/4, y + h/4, w/2, h/2)


# Make the canvas
width = 1000
height = 1000
newPage(width, height)

# Establish how many columns you want in your grid
num_columns = 8
# Establish how many rows you want in your grid
num_rows = 8
# Calculate how big the rectangles are
rect_width = width / num_columns
rect_height = height / num_rows

# Set thickness of stroke
strokeWidth(12)
stroke(0)
# Set no fill
fill(None)

# Loop through each column to make your first row of squares
for column_number in range(num_columns):
    # Each time you do that ^, also loop through rows
    for row_number in range(num_rows):
        # Figure out the position of the rectangle
        x = column_number * rect_width
        y = row_number * rect_height
        make_custom_shapes(x, y, rect_width, rect_height)

# saveImage("~/Desktop/test.pdf")

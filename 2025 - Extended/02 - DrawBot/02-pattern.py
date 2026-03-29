from random import random, randint

# Set the size of the canvas
width = 1000
height = 1000

# Define some parameters
inset = 1
num_columns = 10
num_rows = 10
rect_width = width / num_columns
rect_height = height / num_rows

# Use the size you defined earlier
newPage(width, height)

# Loop through each column
for column_number in range(num_columns):
    # Loop through each row every time you get to a new column
    for row_number in range(num_rows):
        # Set some random strokes and filles
        stroke(random(), random(), random())
        strokeWidth(2)
        fill(random(), random(), random())
        # Calculate where the bottom-left should be for each rectangle
        x = column_number * rect_width
        y = row_number * rect_height
        # Make the rectangle
        rect(x, y, rect_width, rect_height)
        # Establish an if/else conditional to decide whether to add some other stuff in the mix
        if inset < column_number < num_columns - inset and inset < row_number < num_rows - inset:
            fill(0)
            stroke(None)
            this_rect_width = 50
            this_rect_height = 50
            rect(
                x - this_rect_height/2, 
                y - this_rect_height/2, 
                this_rect_width, 
                this_rect_height
                )
        
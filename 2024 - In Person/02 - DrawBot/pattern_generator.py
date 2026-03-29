# Make a page
newPage(1920, 1080)
my_width = width()
my_height = height()

# Divide up the width and height into units
multiplicity = 11
x_units = my_width / multiplicity
y_units = my_height / multiplicity

# Choose a density for the random stuff below
density = 1

# Function to make a set of shapes
def make_module(w, h):
    # Make bottom oval
    if random() < density:
        fill(1)
        oval(0, 0, w, h/2)
    # Make top-left rectangle
    if random() < density:
        fill(random(), random(), 1)
        rect(0, h/2, w/2, h/2)
    # Make the top-right oval
    if random() < density:
        fill(1, random(), random())
        oval(w/2, h/2, w/2, h/2)

# Make a function that draws a whole column
def make_column(x_pos):
    for row in range(int(my_height/y_units)):
        y_pos = row*y_units
        with savedState():
            translate(x=x_pos, y=y_pos)
            # Within the column, draw your special module
            make_module(x_units, y_units)

# Make a black background
fill(0)
rect(0,0,width(), height())

# Loop through the columns
for column in range(int(my_width/x_units)):
    print(f"Establishing a new column {column}")
    x_pos = column * x_units
    with savedState():
        # Make a column, using our function above
        make_column(x_pos)
        
saveImage("_output/pattern.png")

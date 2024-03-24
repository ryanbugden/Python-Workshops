newPage(1920, 1080)
my_width = width()
my_height = height()

x_units = my_width / 30
y_units = my_height / 30

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

def make_column(x_pos):
    for row in range(int(my_height/y_units)):
        y_pos = row*y_units
        with savedState():
            translate(x=x_pos, y=y_pos)
            make_module(x_units, y_units)


fill(0)
rect(0,0,width(), height())
for column in range(int(my_width/x_units)):
    print(f"Establishing a new column {column}")
    x_pos = column * x_units
    with savedState():
        make_column(x_pos)

from random import choice

# Make a list of color values: red, green, blue.
my_colors = [(1,0,0), (0,1,0), (0,0,1)]

# Choose a color tuple, *unpack it, and set the fill
fill(*choice(my_colors))
# Make a rectangle
rect(50,50,400,400)
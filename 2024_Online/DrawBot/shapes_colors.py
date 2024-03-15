# Choose a width and height
my_width  = 1920
my_height = 1920

# Make a function to convert RGB to DrawBot color
def convert_from_rgb(color_value):
    # The magic number we use to convert RGB
    rgb = 255
    new_value = []
    for n in color_value:
        new_value.append(n/rgb)
    return tuple(new_value)

# Start a new page
newPage(my_width, my_height)

# Choose an RGB color value
rgb_value = (255, 36, 100)
# Convert it to a DrawBot-friendly color value
db_color_value = convert_from_rgb(rgb_value)

# Set the fill to our RGB color
# Asterisk is necessary to get rid of () from tuple
fill(*db_color_value)
# Make a rectangle background
rect(0, 0, my_width, my_height)

# Set the fill to blue
fill(0, 0, 1)
# Make a rectangle
rect(260, 320, 500, 300)

# Set the fill to yellow
fill(1, 1, 0)
# Make a oval
oval(60, 500, 600, 336)

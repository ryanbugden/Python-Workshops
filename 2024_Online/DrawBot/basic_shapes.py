# Set width and height
my_width  = 1920
my_height = 1920

rgb = 255

rgb_value = (255, 36, 100)
new_value = []
for n in rgb_value:
    new_value.append(n/255)
print(new_value)

# Start a new page
newPage(my_width, my_height)

# Set the fill to red
fill(255/rgb, 0/rgb, 0/rgb, 1)

# Make a rectangle the size of the page
rect(0, 0, my_width, my_height)
# Set the fill to blue
fill(0.4, 1, 0.2, 0.5)
# Make a rectangle
rect(260, 320, 500, 300)
stroke(1)
strokeWidth(40)
# Make a oval
oval(60, 500, 600, 336)

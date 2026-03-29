# Make a collection of nice colors
my_colors = [
            (1,0,0),
            (1,1,0),
            (1,0,1),
            (0,0,1),
            (0,1,0),
            ]
# Choose one at random
color = choice(my_colors)
# Print the color in its original form
print(color)
# Print the color, unpacked from the tuple
print(*color)
# Start with an empty list of coordinates
my_coords = []
# Loop through 10 pages
for page_number in range(100):
    newPage()
    # Make a random start point and end point
    x1, y1 = randint(0, 500), randint(0, 500)
    x2, y2 = randint(500, 1000), randint(500, 1000)
    # Add those coordinates to our list
    my_coords.append(((x1, y1), (x2, y2)))
    # Set the stroke to black, with a 5 pt thickness
    stroke(0)
    strokeWidth(5)
    # Draw all lines, including previous lines, 
    # because our list keeps getting bigger with each page.
    for coord1, coord2 in my_coords:
        line(coord1, coord2)
    
# Save all pages together as a GIF
saveImage("_output/cumulative_lines.gif")
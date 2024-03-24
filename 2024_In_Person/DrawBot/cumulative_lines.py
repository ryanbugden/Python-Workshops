
my_coords = []
for page_number in range(10):
    newPage()
    x1, y1 = randint(0, 500), randint(0, 500)
    x2, y2 = randint(500, 1000), randint(500, 1000)
    stroke(0)
    strokeWidth(5)
    # Make previous lines again
    for coord1, coord2 in my_coords:
        line(coord1, coord2)
    # Make new line and store it
    line((x1, y1), (x2, y2))
    my_coords.append(((x1, y1), (x2, y2)))
    
saveImage("cumulative_lines.pdf")
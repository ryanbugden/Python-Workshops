newPage(1920, 1080)

cols = 30
rows = 15
col_width = width()/cols
row_height = height()/rows

letters = "qwertyuiopasdfghjklzxcvbnm"
letters = letters.upper()

# Make a grid of columns and rows
for col in range(cols):
    for row in range(rows):
        # Draw the rectangles, get the x and y coords
        fill(None)
        stroke(0)
        x = col_width*col
        y = row_height*row
        rect(x, y, col_width, row_height)
        
        # Draw the letters
        stroke(None)
        fill(0)
        fontSize(50)
        text(choice(letters), (x + col_width/2, y + 17), "center")
    
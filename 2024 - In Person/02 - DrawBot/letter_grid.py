# Make a new widescreen page
newPage(1920, 1080)

# Decide how many columns and rows you want.
cols = 30
rows = 15
# Calculate the column width and row height
col_width = width() / cols
row_height = height() / rows

# Make a string with some letters to choose from
letters = "qwertyuiopasdfghjklzxcvbnm"
# Make it uppercase
letters = letters.upper()

# Make a grid of columns and rows
for col in range(cols):
    for row in range(rows):
        fill(None)
        stroke(0)
        # Calculate the x and y for each rectangle
        x = col_width * col
        y = row_height * row
        rect(x, y, col_width, row_height)
        
        # Draw the letters, centered on the cells
        fill(0)
        stroke(None)
        fontSize(50)
        text(choice(letters), (x + col_width / 2, y + 20), "center")
    
saveImage("_output/letter_grid.pdf")
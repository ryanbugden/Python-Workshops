# Defining our variables
w = 2000
h = 1000
amount_per_row = 14
amount_per_col = 13

# Defining other variables with math
oval_width = w / amount_per_row
oval_height = h / amount_per_col

# Make the page
newPage(w, h)

# Loop through each oval in the row
for row_i in range(amount_per_row):
    print("Starting with row slot #:", row_i)
    # Within that loop, look through each oval in the column
    for col_i in range(amount_per_col):
        print("Making an oval in column slot #:", col_i)
        x = row_i * oval_width
        y = col_i * oval_height
        oval(x, y, oval_width, oval_height)
    print()
    
# Save as pdf
saveImage("~/Desktop/oval_stuff.pdf")
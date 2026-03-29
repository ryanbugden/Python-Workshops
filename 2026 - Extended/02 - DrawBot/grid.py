def star(x, y, w, h):
    path = BezierPath()
    path.moveTo((x, y))
    path.lineTo((x + w/3, y + h/3))
    path.lineTo((x, y + h/3))
    path.lineTo((x + w/2, y + h))
    path.lineTo((x + w, y + h/3))
    path.lineTo((x + w, y + h/3))
    path.lineTo((x + w, y))
    path.closePath()
    drawPath(path)
    
def random_shape(x, y, w, h):
    list_of_functions = [rect, oval, star]
    choice(list_of_functions)(x, y, w, h)
    
# Make a function
def make_module(x, y, w, h, page_width, page_height):
    if x > page_width/2 or y < page_height/2:
        fill(1,0,0,1)
        random_shape(x, y, w, h)
    else:
        fill(0,0,1,1)
        star(x, y, w, h)
    


width = 1920
height = 1080
margin = 120
# Establish how many rows and columns we want
cols = 5
rows = 38
# Based on the overall width, and amount of columns, calculate oval width
module_width = (width - margin*2) / cols
# Based on the overall height, and amount of rows, calculate oval height
module_height = (height - margin*2) / rows


newPage(width, height)
# Loop horizontally along each column, according to how many columns we established
for column in range(cols):
    print(column)
    # Loop vertically along each row, according to how many rows we established
    for row in range(rows):
        # Calculate the position, where we’re at
        x = column * module_width + margin
        y = row * module_height + margin
        # Within that position, make an oval
        make_module(x, y, module_width, module_height, width, height)
        
saveImage("ovals.pdf")
        
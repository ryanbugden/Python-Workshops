my_text = "Hello class, this is how you loop."
# Split text into a list of separate words
list_of_words = my_text.split()

# Drag and drop an otf file here to get its path
font_path = 'path/to/font.otf'

# Loop through each of the words in the list
for word in list_of_words:
    # For each word, make a new page
    newPage('LetterLandscape')
    w = width()
    h = height()
    
    # Set font
    font(font_path)
    fontSize(270)
    # Set fill to red
    fill(1,0,0,1)
    # Set stroke to black
    stroke(0)
    # Draw the text in the middle of the page
    text(word, (w/2, h/2), align='center')

saveImage("~/Desktop/message.pdf")
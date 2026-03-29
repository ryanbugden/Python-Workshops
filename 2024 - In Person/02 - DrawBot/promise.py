# Write a message
my_message = "Hello, class, Python is fun, I promise."
# Split it into separate words
print(my_message.split())

# Set up some fonts to choose from
font_names = ['Helvetica', 'Times New Roman', 'Courier']

# Loop through each word
for word in my_message.split():
    newPage('LetterLandscape')
    frameDuration(1/2)
    my_width = width()
    my_height = height()
    # Make a background
    fill(0)
    rect(0, 0, my_width, my_height)
    # Choose a random font
    font(choice(font_names))
    fontSize(100)
    fill(random(), 0, random())
    # Draw the text in the center of the page
    text(word, (my_width/2, my_height/2), align='center')

# Save all pages as 1 GIF
saveImage("_output/promise.gif")
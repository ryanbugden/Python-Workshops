my_message = "Hello, class, Python is fun, I promise."
print(my_message)
print(my_message.split())

font_names = ['Helvetica', 'Times New Roman']

for word in my_message.split():
    newPage('LetterLandscape')
    frameDuration(1/2)
    my_width = width()
    my_height = height()
    fill(1)
    rect(0, 0, my_width, my_height)
    font(choice(font_names))
    fontSize(100)
    fill(random(), 0, random())
    text(word, (my_width/2, my_height/2), align='center')

saveImage("promise.gif")
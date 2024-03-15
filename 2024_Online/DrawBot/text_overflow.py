my_text = "Hello class, this is how you loop. "
# Make my text super long, so I have text to overflow onto multiple pages
my_text *= 3000

# Decide on a margin
margin = 20

# Start with all text
leftover_text = my_text
while leftover_text:
    # Choose the size with plain English
    newPage('LetterLandscape')
    # textBox returns the leftover_text
    # until it is empty -> kick out of while loop
    leftover_text = textBox(leftover_text, (margin, margin, width() - margin*2, height() - margin*2), align='left')
my_list = ["one", "two", "three"]

# Start a count at 0
counter = 0 
for item in my_list:
    # Check to see if index is odd or even
    if counter % 2 != 0:
        print(item)
    # Add to the counter for next go-round
    counter += 1
    
# What I have on my desk
desk_items = ["Sharpie", "Keyboard", "Mouse"]

# Make a function to search my desk
def do_i_have_it_on_my_desk(what_looking_for):
    # Loop through every item in desk_items
    for pizza in desk_items:
        # If one matches, tell me!
        if pizza == what_looking_for:
            print("FOUND IT!")
            # End the function if we found it.
            return
    # If I still haven't found it...
    print("Nothing was found")
            
do_i_have_it_on_my_desk("Mouse")
                
            
        
        

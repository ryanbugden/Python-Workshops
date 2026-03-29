favorite_numbers = {
    # key    : value
    "Kevin"  : 10, 
    "Eunice" : 64, 
    "Mel"    : 92
    }
    
print("Kevin’s favorite number is:", favorite_numbers["Kevin"])
print()  # Print an empty line

# Booleans (True or False)
print(2 > 10,  "← Is 2 greater than 10?")
print(2 < 10,  "← Is 2 less than 10?")
print(2 <= 10, "← Is 2 less than or equal to 10?")
print(2 == 10, "← Is 2 equal to 10?")
print(2 != 10, "← Is 2 not equal to 10?")

print()
# Use if/elif/else to see what kind of number Kevin likes.
if favorite_numbers["Kevin"] > 10:
    print("He has a cool favorite number.")
elif favorite_numbers["Kevin"] == 10:
    print("Acceptable choice.")
else:
    print("Number is too low.")

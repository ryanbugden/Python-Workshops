letter = "n"

# Make a function that tries to guess if a letter from a string is uppercase or lowercase
def check_case(string):
    if string == string.lower():
        return "lowercase"
    else:
        return "uppercase"
        
# Print the result from the function
print(check_case(letter))
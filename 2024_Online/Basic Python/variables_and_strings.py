# Variables
name = "Jeremy"

print(name)
print(name.swapcase())
print(name.replace("J", "M"))

# Tell me the name
print(name)
# Is it all caps?
print(name.isupper())
# Make the name all caps
name.upper()
# Tell me the name again
print(name)
# Is it all caps?
print(name.isupper())

# Get my glyph name
my_glyph_name = "g"
## Doesn't work because you need to set the variable again
# my_glyph_name.upper()
# Make it uppercase
my_glyph_name = my_glyph_name.upper()
print(my_glyph_name)


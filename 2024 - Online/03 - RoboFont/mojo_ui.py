# menuTitle: Slant Font
# shortCut: shift + command + control + o

from mojo.UI import AskString

# Open the little UI, get user input, and store the string in a variable
user_input = AskString("How much do you want to slant your font?", value="25")
# Convert the string to an integer
user_input = int(user_input)
# Confirm that it's an integer
print(type(user_input))

# Then do whatever you want with this number...
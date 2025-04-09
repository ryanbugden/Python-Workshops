# Make a dict and put it in a variable
crazy_name = {
    "Ryan": "Blue",
    "Kai": "Green"
    }
# You can get just the keys of the dict...
print(crazy_name.keys())
# ... or just the values
print(crazy_name.values())
# ... or nice pairings of keys and values together, ready to loop through, like...
print(crazy_name.items())
# ... this
for name, color in crazy_name.items():
    print(name, color)
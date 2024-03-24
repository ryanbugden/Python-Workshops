# Let's decide where to eat for lunch
# Store votes in a dictionary
restaurant_votes = {
    "Shake Shack": ["Amanda", "Hui", "Mina"],
    "Bar Verde": ["Javier", "JJ"]
    }

# Print the result, by testing the lengths of the lists.
if len(restaurant_votes["Shake Shack"]) > len(restaurant_votes["Bar Verde"]):
    print("We're going to Shake Shack")
else:
    print("Bar Verde it is.")

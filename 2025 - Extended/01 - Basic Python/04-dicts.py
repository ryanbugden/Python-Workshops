# Dictionaries! Each "key" gets a "value"
favorite_numbers = {"Xinyuan": 8, "Yihuang": 4}

# Change info in the dictionary
favorite_numbers["Yihuang"] = 12
print(favorite_numbers)
# Check info in the dictionary
print("Is Yihuang’s favorite number 12?", favorite_numbers["Yihuang"] == 12)

# Check some more, with conditionals
if favorite_numbers["Yihuang"] >= 12:
    print("Yihuang’s favorite number is greater than or equal to 12")
else:
    print("Yihuang’s favorite number is NOT greater than or equal to 12")
        
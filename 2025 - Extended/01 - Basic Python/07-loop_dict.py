object_colors = {
    # Key       # Value
    "Backpack": "", 
    "Laptop": "", 
    "iPhone": ""
    }
    
print(object_colors)

# Loop through the dictionary
for object_name, color in object_colors.items():
    # Change every "value" to "Purple"
    object_colors[object_name] = "Purple"
    # See how the dictionary changes as you loop
    print(object_colors)
    
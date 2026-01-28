# Make a function that cuts names in half
def cut_name_in_half(name):
    half_length_of_name = int(len(name)/2)
    print(name[0:half_length_of_name])

# Run the function on a string
cut_name_in_half("Gabrielle")
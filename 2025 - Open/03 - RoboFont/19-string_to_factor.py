from mojo.UI import AskString


def string_into_factor(string):
    '''
    This is a hackey weird function that takes a random string input and tries to 
    convert it into an interpolation factor (isotropic (float) or anisotropic (tuple))
    '''
    # If there’s space, make into a tuple
    if " " in string:
        to_tuple = []
        for piece in string.split():
            to_tuple.append(float(piece))
        factor = tuple(to_tuple)
    # If no space, just turn it into a number
    else:
        factor = float(string)
    return factor
        
# Pop a window up to ask for the factor
factor = AskString("Enter here")
# Convert the input to a helpful number or tuple of numbers
factor = string_into_factor(factor)
print(factor, type(factor))

## Use it for interpolation down here...


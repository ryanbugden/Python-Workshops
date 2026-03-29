# Make a general function, not related to the Bicycle below
def ride():
    print("General riding (not related to Bicycle object).")

# Make an object template for Bicycle
class Bicycle():
    
    # ... that starts with an empty name attribute
    def __init__(self):
        self.name = ""
        
    # ... and has a function for riding
    def ride(self):
        print(self.name, "bike riding")

    
# Ride in general, not the bicycle
ride()

# # Establish two bicycles, set their names, and make them ride
bike_1 = Bicycle()
bike_1.name = "Bessie"
bike_2 = Bicycle()
bike_2.name = "Bradley"
bike_1.ride()
bike_2.ride()


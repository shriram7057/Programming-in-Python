# Creating a parent class named Vehicle
class Vechicle:  
    name = "TATA"  # Global variable 

    def display(self):                      # Method to display the vehicle name

        print("Name:", self.name)  

class Category(Vechicle):                   # Creating a child class named Category that inherits from Vehicle

    price = 150000  # Global Variable

    def display_price(self):                # Method to display the price of the vehicle
 
        print("Price is:", self.price)  

# Creating an instance/objects of Category class
c1 = Category()
  
c1.display_price()  # Calling the method to display price

# Accessing class attributes directly

print("Name of the Vehicle:", Vechicle.name) 

print("Price of the Vehicle:", Category.price)  

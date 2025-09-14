class car:
    def __init__(self):

        #initialize the car with Default Attributes 
        self.make="TOYOTA"
        self.model="corolla"
        self.year="2020"

# creating an instance for default constructor

c1=car()
print("Car Company is :",c1.make)
print("Car Model is :",c1.model)
print("Car Year is :",c1.year)

# A default constructor in Python is a constructor that takes no arguments (except self).
# It is automatically called when an object of the class is created.
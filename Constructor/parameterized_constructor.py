class car: # defining a class named car
    def __init__(self,make,model,year):

        #initialize the car with specific attributes 
        self.make=make
        self.model=model
        self.year=year

#Creating an instance using parameterized conatructor

c1=car("Honda","civil",2002)

# printing the car details  
print("Car Company is :",c1.make)
print("Car Model is :",c1.model)
print("Car Year is :",c1.year)


# A parameterized constructor in Python is a constructor (__init__ method) 
# that accepts parameters to initialize an object with specific values.

class Student:
    # Constructor (Initializer) method
    def __init__(self):
        print("Student object is created with non-parameterized Constructor!")
    
    # Destructor method
    def __del__(self):
        print("Destructor is called, Student object is deleted!")

# Creating the first Student object
s1 = Student()

# Creating the second Student object
s2 = Student()

# print("Student objects is created")
# Deleting the second Student object explicitly

del s2  # keyword are used to destruct the object

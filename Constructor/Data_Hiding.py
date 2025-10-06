class Student:
    __a = 10  # Private variable
    b = 20    # Public variable

    def init(self):
        print("Constructor called")

    def __private_method(self):
        print("I am a private method")

    def public_method(self):
        print("I am a public method")
        print("Calling private method inside a public method")
        self.__private_method()  # Accessing private method inside the class

# Creating an object of Student class
s1 = Student()

# Accessing public variable
print("Public variable accessed outside class:", s1.b)

# Accessing private variable (will cause an error)
# print("Private variable:", s1.__a)  # Uncommenting this will cause an error

# Accessing private method (will cause an error)
# s1.__private_method()  # Uncommenting this will cause an error

# Accessing public method
print("Calling public method outside class")
s1.public_method()
# • The idea is to allow the caller to specify the argument name with values so 
# that the caller does not need to remember the order of parameters

def Student(FirstName,lastName):
    print(FirstName,lastName)

#Keywords arguments

Student(FirstName="Shriram",lastName="Lahane")
Student(lastName="Lahane",FirstName="Shriram")
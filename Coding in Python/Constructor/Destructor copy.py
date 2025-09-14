class Student:
    def __init__(self):
        print("Student object is created with non parameterizes Constructor!")
    def __del__(self):
        print("Destructor is called Student object is deleted!")
s1=Student()
s2=Student()
del s2
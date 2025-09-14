class Student:
    def __init__(self):   #Default Method!
        print("This is non Parameterized Constructor!")

    def show(self,name):
        print("Hello",name)
s1=Student()
s1.show("Shriram")
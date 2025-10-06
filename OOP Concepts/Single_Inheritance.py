class A :
    def show(self):
        print("This is show method!")
class B(A):
    def display(self): 
        print("This is display method!")
b1=B()
b1.display()
b1.show()
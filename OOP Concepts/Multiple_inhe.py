class A:
    def showA(self):
        print("This is show method of A")
class B():
    def showB(self):
        print("This is show method of B")
class C(A,B):
    def showC(self):
        print("This is show method of C")

c1=C()

c1.showA()
c1.showB()
c1.showC()
#Hierarchical Inheritance 
class A: 
    def display_A(self): 
        print("display_A method of class A"); 
 
class B(A): 
    def display_B(self): 
        print("display_B method of class B"); 
 
class C(A): 
    def display_C(self): 
        print("display_C method of class C"); 
 
b1=B(); 
c1=C(); 
print("***Object b1****"); 
b1.display_A(); 
b1.display_B(); 
print("***Object c1****"); 
c1.display_A(); 
c1.display_C(); 
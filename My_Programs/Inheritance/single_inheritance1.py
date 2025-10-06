#single inheritance 
class Dog:
    def __init__(self,name):
        self.name=name
    def display_name(self):
        print(f"Dogs name :{self.name}")

class Labrador(Dog): # single inheritance 
    def sound(self):
        print("Labrador woofs!")

l1=Labrador("Moti!!")
l1.display_name()
l1.sound()
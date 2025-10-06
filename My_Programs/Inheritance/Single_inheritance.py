# The process of creating new class by using the concepts of old class is known as Inheritance 

# - Syntax:  
#  class A:  
#   #properties of class A  
#  class B(A):  
#   #properties of class B   
#   #Inherited properties of class A   

  
# Single Inheritance: - To create new class from only one base class is known as Single Inheritance. 

class Gmail:
    def send_email(self, msg):
        print("Sending {} from Gmail".format(msg))

    class Yahoo:
        def send_email(self, msg):
            print("Sending {} from Yahoo".format(msg))


class Email:
    provider = Gmail()  

    def set_provider(self, p):
        self.provider = p 

    def send_email(self, msg):
        self.provider.send_email(msg) 


client = Email()
client.send_email("Hello")  

client.set_provider(Gmail.Yahoo())  
client.send_email("Hello") 

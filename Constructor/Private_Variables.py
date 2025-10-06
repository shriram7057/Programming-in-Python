# Class Definition
class A:
    def __init__(self, News="Welcome"):  # Constructor with default parameter "Welcome"
        self.__s = News  # Private instance variable 
        print("In __init__, value stored:", self.__s)  # Prints message when object is created

    def print1(self):  # Method to print the stored message
        print("In print1 method:", self.__s)


# Main function to execute the program
def main():
    a = A("Bhagyesh")  # Object 'a' is created with custom value "Bhagyesh"
    a.print1()  # Calls print1() method of object 'a'

    b = A("Greetings")  # Object 'b' is created with custom value "Greetings"
    b.print1()  # Calls print1() method of object 'b' to print its stored value


# Calling the main function
main()

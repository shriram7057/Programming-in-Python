class test:
      'This is sample class called test!'

      def __init__(self):
            print("Hello form__init__method")

    # Class built in attributes!
            print("class name is:",test.__name__) 
            print("its doc string is:",test.__doc__) 
            print("Tuple having base classes",test.__bases__) 
            print("class Namespace  is:",test.__dict__) 
t1=test()
t1
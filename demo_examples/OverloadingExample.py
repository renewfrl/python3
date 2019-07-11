#!/usr/local/bin/python3

class Human(object):

    def sayHello(self, name=None):

        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')


# Create instance
obj = Human()

# Call the method v1
obj.sayHello()

# Call the method with a parameter
obj.sayHello('to all')
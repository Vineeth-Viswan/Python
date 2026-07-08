class Example:
    def __init__(self, internal, private):
        self._internal = internal
        self.__private = private

class Parent:
    def __init__(self):
        self.__data = "Parent data"
    
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__data = "Child data"  # This will override the parent's _data variable

def main():
    #obj = Example("This is an internal variable", "This is a private variable")
    #print(obj._internal)  # Accessing the internal variable
    #print(obj.__private)  # This will raise an AttributeError
    #print(obj.__dict__)  # Accessing the internal variable using name mangling
    #print(obj._Example__private)  # Accessing the private variable using name mangling

    child = Child()
    print(child.__dict__)  # Accessing the child's _data variable

    parent = Parent()
    print(parent.__dict__)  # Accessing the parent's _data variable

if __name__ == "__main__":
    main()

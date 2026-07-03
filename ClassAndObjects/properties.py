
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    
    @property
    def area(self):
        return 3.14 * self._radius ** 2
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @radius.deleter
    def radius(self):
        print("Deleting radius...")
        del self._radius
    

def __main__():
    circle = Circle(5)
    print("Testing Circle class with radius:", circle.radius)
    print("Testing Circle class with area:", circle.area)

    circle.radius = 10
    print("Updated radius:", circle.radius) 
    print("Updated area:", circle.area)

    del circle.radius

    try:
        print(circle.radius)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    __main__()
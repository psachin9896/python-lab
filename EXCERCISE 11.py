class Polygon:
    """ created a constructor class with no of sides"""
    def __init__(self, total_sides):
        self.total_sides = total_sides
        """storing size in a list to print size of the side with index"""
        self.sides = []

    def inputSides(self):
        """using list comprehension to print the index and length of the each side of the polygon."""
        for i in range(self.total_sides):
            self.sides.append(int(input("please enter length of side:")))

    def despSide(self):
        """displaying the index and size of the each polygon side"""
        for index, value in enumerate(self.sides):
            print("Index : {}  Value : {}".format(index, value))

class Triangle(Polygon):
    """class inherited from Polygon class"""
    def __init__(self):
        Polygon.__init__(self,3)

    def findPerimeter(self):
        return sum(self.sides)

    def findArea(self):
        a, b, c = self.sides
        s = (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        return area

class EquilateralTriangle(Triangle):
    """ created a subclass of triangle """
    def __init__(self):
        Triangle.__init__(self)

    def findPerimeter(self ):
        return 3 * self.sides[0]

if __name__ == "__main__":
    T1 = Triangle()
    T1.inputSides()
    E1 = EquilateralTriangle()
    E1.inputSides()
    perimeter = T1.findPerimeter()
    print("the perimeter of the triangle is {}".format(perimeter))
    perimeter_2 = E1.findPerimeter()
    print("the perimeter of the equlattriangle is {}".format(perimeter_2))














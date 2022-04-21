class Polygon:
    """ created a constructor class with nn of sides"""
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
        perimeter = sum(self.sides)
        return perimeter

    def findArea(self):
        a, b, c = self.sides
        s = (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        return area

if __name__ == "__main__":
    t1 = Triangle()
    t1.inputSides() # creating an object for method of polygon class
    perimeter = t1.findPerimeter()
    print(" the perimeter of the triangle is {}".format(perimeter))
    area = t1.findArea()
    print(" Area of the triangle is {}".format(area))







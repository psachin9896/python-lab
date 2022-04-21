class Polygon:
    def __init__(self, total_sides):

        self.total_sides = total_sides
        self.sides = []

    def inputSides(self):
        """using list comprehension to print the index and length of the each side of the polygon."""
        print("input sides")
        for i in range(self.total_sides):
            self.sides.append(int(input("enter the length of the side:")))
        print(self.sides)

    def dispSides(self):
        """displaying the index and size of the each polygon side"""
        for index, side in enumerate(self.sides):
            print("index: {} side: {}".format(index,side))



p1 = Polygon(4)
p1.inputSides()
p1.dispSides()
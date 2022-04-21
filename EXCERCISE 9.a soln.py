
class Polygon:
    def __init__(self,no_of_sides):
        self.n = no_of_sides # only one parameter to the constructor class

    def inputSides(self):
        """using list comprehension to print the index and length of the each side of the polygon."""

        print("input sides")
        self.sides = [int(input("enter side" + " " +str(i+1)+" : " )) for i in range(self.n)]
        print(self.sides)

    def dispSides(self):

        # displaying the index and size of the each polygon side
        print(" the size of the each polygon side is :")
        for i in range(self.n):
            print("side", i + 1, "is", self.sides[i])

p1 = Polygon(4)
p1.inputSides()
p1.dispSides()


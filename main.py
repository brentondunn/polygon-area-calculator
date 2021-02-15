from math import sqrt


class Quadrilateral(object):
    def __init__(self, side1, side2, side3, side4):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4

    def perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4

    def area(self):
        return self.side1 * self.side2

    @staticmethod
    def get_shape():
        return 'quadrilateral'


class Square(Quadrilateral):
    def __init__(self, side1, side2=0, side3=0, side4=0):
        side2 = side1
        side3 = side1
        side4 = side1
        super().__init__(side1, side2, side3, side4)

    @staticmethod
    def get_shape():
        return 'square'


class Rectangle(Quadrilateral):
    def __init__(self, side1, side2, side3=0, side4=0):
        side3 = side1
        side4 = side1
        super().__init__(side1, side2)

    @staticmethod
    def get_shape():
        return 'rectangle'


class Parallelogram(Quadrilateral):
    def __init__(self, side1, side2, side3=0, side4=0):
        side3 = side1
        side4 = side1
        super().__init__(side1, side2)

    @staticmethod
    def get_shape():
        return 'parallelogram'


class Trapezoid(Quadrilateral):

    def __init__(self, top, bottom, left, right):
        """
        :param top: top bases
        :type top: float
        :param bottom: bottom base
        :type bottom: float
        :param left: left leg
        :type left: float
        :param right: left leg
        :type right: float
        """
        super().__init__(top, bottom, left, right)

    def perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4

    def area(self):
        height = sqrt(
            (self.side1 + self.side4 - self.side2 + self.side3) *
            (-self.side1 + self.side4 + self.side2 + self.side3) *
            (self.side1 - self.side4 - self.side2 + self.side3) *
            (self.side1 + self.side4 - self.side2 - self.side3) /
            (4 * (self.side1 - self.side2)**2)
        )
        return (self.side1 + self.side2) / 2 * height

    @staticmethod
    def get_shape():
        return 'trapezoid'


class Triangle(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter()
        return sqrt(p * (p-self.a) * (p-self.b) * (p-self.c))

    @staticmethod
    def get_shape():
        return 'triangle'


def calculate(shape):
    calc = input('What calculation do you want to do? ')
    if calc == 'perimeter':
        return shape.perimeter()
    if calc == 'area':
        return shape.area()


doAgain = True
while doAgain:
    numberOfSides = int(input('How many sides does the object have? '))
    if numberOfSides == 3:
        a = int(input('How long is its shortest side? '))
        b = int(input('How long is its medium side? '))
        c = int(input('How long is its longest side? '))
        givenShape = Triangle(a, b, c)
    elif numberOfSides == 4:
        shape = input('What object is it? ')
        if shape == 'square':
            sideLength = int(input('What side length does it have? '))
            givenShape = Square(sideLength)
        elif shape == 'rectangle':
            width = int(input('What width does it have? '))
            length = int(input('What length does it have? '))
            givenShape = Rectangle(width, length)
        elif shape == 'trapezoid':
            topBase = int(input('What is the length of the top base? '))
            bottomBase = int(input('what is the length of the bottom base? '))
            left = int(input('What is the length of the left leg? '))
            right = int(input('What is the length of the right leg? '))
            givenShape = Trapezoid(topBase, bottomBase, left, right)
        elif shape == 'parallelogram':
            width = int(input('What width does it have? '))
            length = int(input('What length does it have? '))
            givenShape = Parallelogram(width, length)

    print(calculate(givenShape))
    askAgain = input('Do you want to find the area or perimeter of another shape? (Y/N) ')
    if askAgain == 'Y' or askAgain == 'y':
        continue
    else:
        doAgain = False


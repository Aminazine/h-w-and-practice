# 33. Создать два класса: Окружность и Точка. Создать в классе окружности метод,
# который принимает в качестве параметра точку и проверяет находится ли данная точка внутри окружности.

class Shape(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point(Shape):

    def __init__(self, x, y):
        Shape.__init__(self, x, y)

class Circle(Shape):

    def __init__(self, x, y, r):
        Shape.__init__(self, x, y)
        self.r = r

    def check_point(self, point):
        import math
        if (math.sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)) <= self.r:
            print("\t""Yes. The point is included in the circle""\n")
        else:
            print("\t""No. The point is not included in the circle""\n")

crcl = Circle(2, 1, 5)
print("Center coordinates (%g, %g) of the circlec with radius = %g" % (crcl.x, crcl.y, crcl.r))
pnt = Point(3, 3)
print("Point coordinates is (%g, %g)" % (pnt.x, pnt.y))
crcl.check_point(pnt)

crc2 = Circle(1, 3, 2.5)
print("Center coordinates (%g, %g) of the circlec with radius = %g" % (crc2.x, crc2.y, crc2.r))
pnt2 = Point(1, 2)
print("Point coordinates is (%g, %g)" % (pnt.x, pnt.y))
crc2.check_point(pnt2)

# 33. Создать два класса: Окружность и Точка. Создать в классе окружности метод,
# который принимает в качестве параметра точку и проверяет находится ли данная точка внутри окружности.

class Parameters(object):

    def __init__(self, absc, ord):
        self.absc = absc
        self.ord = ord


class Point(Parameters):

    def __init__(self, absc, ord):
        Parameters.__init__(self, absc, ord)


class Circle(Parameters):

    def __init__(self, absc, ord, rad):
        Parameters.__init__(self, absc, ord)
        self.rad = rad

    def check_point(self):
        import math
        if (math.sqrt((pnt.absc - crcl.absc) ** 2 + (pnt.ord - crcl.ord) ** 2)) <= crcl.rad:
            print("\t""Yes. The point is included in the circle""\n")
        else:
            print("\t""No. The point is not included in the circle""\n")


crcl = Circle(2, 1, 1)
print("Center coordinates (%g, %g) of the circlec with radius = %g" % (crcl.absc, crcl.ord, crcl.rad))
pnt = Point(3, 3)
print("Point coordinates is (%g, %g)" % (pnt.absc, pnt.ord))
crcl.check_point()

crcl = Circle(1, 3, 2.5)
print("Center coordinates (%g, %g) of the circlec with radius = %g" % (crcl.absc, crcl.ord, crcl.rad))
pnt = Point(1, 2)
print("Point coordinates is (%g, %g)" % (pnt.absc, pnt.ord))
crcl.check_point()

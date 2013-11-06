import math

class Point(object):
    def __init__(self, x, y):
        self.x, self.y = Decimal(x), Decimal(y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

def index_rotation(pointx, pointy):
    p = Point(pointx, pointy)

    for i in range(points):
        total = math.acos(scalar_product(points[-1] - p, points[0] - p) /
                          (norm(points[-1] - p * norm(points[0] - p))))

    return total / 2 * math.pi

def scalar_product(point1, point2):
    return (point1.x * point2.x) + (point1.y * point2.y)

def norm(point):
    return math.sqrt((point.x*point.x) + (point.y*point.y))



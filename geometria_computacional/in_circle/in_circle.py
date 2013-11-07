
class Point(object):
    def __init__(self, x, y):
        self.x, self.y = Decimal(x), Decimal(y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Circle(object):
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

def in_circle(circle, point):
    p1_point_x = circle.p1.x - point.x
    p1_point_y = circle.p1.y - point.y

    p2_point_x = circle.p2.x - point.x
    p2_point_y = circle.p2.y - point.y

    p3_point_x = circle.p3.x - point.x
    p3_point_y = circle.p3.y - point.y

    column1 = pow(p1_point_x, 2) + pow(p1_point_y, 2)
    column2 = pow(p2_point_x, 2) + pow(p2_point_y, 2)
    column3 = pow(p3_point_x, 2) + pow(p3_point_y, 2)

    left = (p1_point_x * p2_point_y * column3) + (p2_point_x * p3_point_y * column1) + (p3_point_x * p1_point_y * column2)
    right = (p1_point_x * p2_point_y * column2) + (p2_point_x * p3_point_y * column3) + (p3_point_x * p1_point_y * column1)

    return True if (left - right) > 0 else False


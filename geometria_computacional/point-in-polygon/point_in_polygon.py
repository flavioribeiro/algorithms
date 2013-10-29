from decimal import *
getcontext().prec = 4

class Point(object):
    def __init__(self, x, y):
        self.x, self.y = Decimal(x), Decimal(y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Segment(object):
    def __init__(self, p1, p2):
        self.p1, self.p2 = p1, p2

def drange(start, stop, step):
    r = start
    while r < stop:
        yield Decimal(r)
        r += Decimal(step)

def inside(polygon, point):
    max_x = max([max(segment.p1.x, segment.p2.x) for segment in polygon]) + 10
    interceptions = 0

    for segment in polygon:
        for x_coord in drange(point.x, max_x, 0.01):
            p = Point(x_coord, point.y)
            if p == segment.p1 or p == segment.p2: return True
            elif point_in_segment(p, segment): interceptions += 1

    return False if interceptions % 2 == 0 else True

def point_in_segment(point, segment):
    m = Decimal(segment.p2.y - segment.p1.y)/(segment.p2.x - segment.p1.x)
    q = segment.p1.y - m * segment.p1.x
    return True if (point.y) == (m*point.x + q) else False


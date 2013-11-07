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

def is_parallel(segment1, segment2):
    m1 = Decimal(segment1.p2.y - segment1.p1.y)/(segment1.p2.x - segment1.p1.x)
    m2 = Decimal(segment2.p2.y - segment2.p1.y)/(segment2.p2.x - segment2.p1.x)

    return m1 == m2

def intersect(p1, p2, p3, p4):
    v1 = vetorial_product(p1, p2, p3)
    v2 = vetorial_product(p1, p2, p4)
    v3 = vetorial_product(p3, p4, p2)
    v4 = vetorial_product(p3, p4, p1)

    return True if (((v1 > 0) and (v2 < 0) or (v1 < 0) and (v2 > 0)) and (v3 > 0) and (v4 < 0 ) or (v3 < 0 ) and (v4 > 0)) else False

def vetorial_product(pi, pj, pk):
    return (pk.x - pi.x)*(pj.y-pi.y) - (pj.x-pi.x)*(pk.y-pi.y)


def intersect_segments(segment1, segment2, point):
    if not intersect(segment1.p1, segment1.p2, segment2.p1, segment2.p2) or is_parallel(segment1, segment2):
        return False
    else:
        determinant = ((segment1.p1.x - segment1.p2.x) * (segment2.p1.y - segment2.p2.y)) - ((segment1.p1.y - segment1.p1.y) * (segment2.p1.x - segment2.p2.x))

        d1 = (segment1.p1.x*segment1.p2.y - segment1.p1.y*segment1.p2.x);
        d2 = (segment2.p1.x*segment2.p2.y - segment2.p1.y*segment2.p2.y);

        x = (d1*(segment2.p1.x - segment2.p2.x) - (d2*(segment1.p1.x - segment1.p2.x))) / det
        y = (d1*(segment2.p1.y - segment2.p2.y) - (d2*(segment1.p1.y - segment1.p2.y))) / det

        print x,y
        return True

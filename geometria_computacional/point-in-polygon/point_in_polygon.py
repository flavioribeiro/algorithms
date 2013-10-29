class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Segment(object):
    def __init__(self, p1, p2):
        self.p1, self.p2 = p1, p2
    def __str__(self):
        return "Segment[(%d, %d), (%d, %d)]" % (self.p1.x, self.p1.y, self.p2.x, self.p2.y)

def inside(polygon, point):
    max_x = max([max(segment.p1.x, segment.p2.x) for segment in polygon]) + 10
    interceptions = 0

    for x_coord in range(point.x, max_x):
        for segment in polygon:
            p = Point(x_coord, point.y)
            if p == segment.p1 or p == segment.p2: return True
            if point_in_segment(Point(x_coord, point.y), segment):
                interceptions += 1

    return False if interceptions % 2 == 0 else True

def point_in_segment(point, segment):
    m = float(segment.p1.x - segment.p2.x)/(segment.p1.y - segment.p2.y)
    q = segment.p1.y - m * segment.p1.x
    return True if (point.y) == (m*point.x + q) else False




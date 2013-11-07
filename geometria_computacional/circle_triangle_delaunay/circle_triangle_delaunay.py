
class Point(object):
    def __init__(self, x, y):
        self.x, self.y = Decimal(x), Decimal(y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

def circle(pointa, pointb, pointc):
    d = 2*( (pointa.x * (pointb.y - pointc.y)) + (pointb.x * (pointc.y - pointa.y)) + (pointc.x * (pointa.y - pointb.y)))
    a2 = pow(pointa.x, 2) + pow(pointa.y, 2)
    b2 = pow(pointb.x, 2) + pow(pointb.y, 2)
    c2 = pow(pointc.x, 2) + pow(pointc.y, 2)

    x = (a2*(pointb.x - pointc.x) + b2*(pointc.x - pointa.x) + c2*(pointa.x - pointb.x)) / d;
    y = (a2*(pointb.y - pointc.y) + b2*(pointc.y - pointa.y) + c2*(pointa.y - pointb.y)) / d;

    print x, y, d


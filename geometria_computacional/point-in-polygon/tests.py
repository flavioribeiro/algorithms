from point_in_polygon import Point, Segment, inside

def test_point_should_be_outside_polygon():
    p1, p2, p3 = Point(10, 10), Point(35, 20), Point(30,40)
    triangle = [Segment(p1, p2), Segment(p2, p3), Segment(p3, p1)]

    point_1 = Point(10, 25)
    assert not inside(triangle, point_1)

def test_point_on_edge_should_be_inside_polygon():
    p1, p2, p3 = Point(10, 10), Point(35, 20), Point(30,40)
    triangle = [Segment(p1, p2), Segment(p2, p3), Segment(p3, p1)]

    point_2 = Point(10, 10) #edge
    assert inside(triangle, point_2)

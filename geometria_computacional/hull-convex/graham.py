def turn(p, q, r):
    return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

def keep_left(hull, r):
    while len(hull) > 1 and turn(hull[-2], hull[-1], r) != 1:
            hull.pop()
    if not len(hull) or hull[-1] != r:
        hull.append(r)
    return hull

def convex_hull(points):
    points = sorted(points)
    l = reduce(keep_left, points, [])
    u = reduce(keep_left, reversed(points), [])
    return l.extend(u[i] for i in xrange(1, len(u) - 1)) or l

# A = [18.95,26.475]
# B = [18.95,39.725]
# C = [25.55,26.475]
# D = [28.35,20.475]
points= ([18.95,26.475],[18.95,39.725],[25.55,26.475],[28.35,20.475])

# deve imprimir A->B->C->D
print convex_hull(points)

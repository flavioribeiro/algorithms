import unittest

def RANDOMIZED_PARTITION(A, p, r):
    x = A[r-1]
    i = p
    for j in range(p, r-1):
        if A[j] <= x:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r-1] = A[r-1], A[i]
    return i

def RANDOMIZED_SELECT(A, p, r, i):
    if p + 1 == r:
        return A[p]
    q = RANDOMIZED_PARTITION(A, p, r)
    k = q - p
    if i == k:
        return A[q]
    elif i < k:
        return RANDOMIZED_SELECT(A, p, q, i)
    return RANDOMIZED_SELECT(A, q, r, i - k)

class RandomizedSelectTest(unittest.TestCase):
    def setUp(self):
        self.data = [1, 7, 3, 5, 0, 9, 4, 6, 2, 8]

    def test_select_minimum(self):
        self.assertEqual(
            0,
            RANDOMIZED_SELECT(self.data, 0, len(self.data), 0)
        )

    def test_select_maximum(self):
        self.assertEqual(
            9,
            RANDOMIZED_SELECT(self.data, 0, len(self.data), 9)
        )

    def test_select_median(self):
        self.assertEqual(
            4,
            RANDOMIZED_SELECT(self.data, 0, len(self.data), 4)
        )
        self.assertEqual(
            5,
            RANDOMIZED_SELECT(self.data, 0, len(self.data), 5)
        )


if __name__ == '__main__':
    unittest.main()

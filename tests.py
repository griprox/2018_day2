from maxima import find_maxima
import unittest
class Test_maxima(unittest.TestCase):
    def test_ez1(self):
        x = [1, 2, 1, 3, 1, 4]
        ans = [1, 3, 5]
        self.assertEqual(find_maxima(x), ans)

    def test_ez2(self):
        x = [1, 2, 5, 7, 4, 5]
        ans = [3, 5]
        self.assertEqual(find_maxima(x), ans)

    def test_sided(self):
        x = [1, 5]
        ans = [1]
        self.assertEqual(find_maxima(x), ans)

    def test_nomaxima(self):
        x = [2, 1]
        ans = []
        self.assertEqual(find_maxima(x), ans)

    def test_equalvals(self):
        x = [1, 2, 2, 1 ,4, 4]
        ans = [5]
        self.assertEqual(find_maxima(x), ans)

if __name__ == '__main__':
    unittest.main()

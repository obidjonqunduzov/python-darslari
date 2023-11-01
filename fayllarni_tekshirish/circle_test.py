import unittest

from circle import get_area, get_perimeter


class CircleTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(get_area(10), 314.159)
        self.assertAlmostEqual(get_area(3),28.27431)
    def test_perimeter(self):
        self.assertAlmostEqual(get_perimeter(10), 62.8318)
        self.assertAlmostEqual(get_perimeter(4), 25.13272)
        
unittest.main()

import unittest

from numbers import get_number

class NumberTest(unittest.TestCase):
	def test_number(self):
		test_number = get_number(4,8,3)
		self.assertEqual(test_number,8)

unittest.main()
import unittest
from subtraction import subtraction
class TestSubtraction(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(subtraction(), 10)

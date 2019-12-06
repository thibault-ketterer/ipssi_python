#!/usr/bin/python3

import unittest
from unnecessary_math import multiply, divide
class TestUM(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_3_4(self):
        self.assertEqual( multiply(3,4), 12)
    def test_strings_a_3(self):
        self.assertEqual( multiply('a',3), 'aaa')
    def test_divide_12_4(self):
        self.assertEqual( divide(12, 4), 3)
    def test_divide_float(self):
        self.assertEqual( type(divide(8, 3)), float)
    def test_divide_by_0(self):
        with self.assertRaises(ZeroDivisionError):
            divide(3 ,0)
if __name__ == '__main__':
    unittest.main()

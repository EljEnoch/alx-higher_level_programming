#!/usr/bin/python3

"""
Unittest for max_integer([..])

"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max(self):
        self.assertEqual(max_integer([1, 8, 3, 4]), 8)
        self.assertEqual(max_integer([25]), 25)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 2, 3, 4, 4]), 4)
        self.assertEqual(max_integer([1, 4.7, 4.8]), 4.8)

if __name__ == '__main__':
    unittest.main()

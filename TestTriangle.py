# -*- coding: utf-8 -*-
"""
Updated Test Cases for classifyTriangle()
"""

import unittest
from Triangle import classifyTriangle

class TestClassifyTriangle(unittest.TestCase):
    
    # Test Equilateral triangle: All sides are equal
    def test_equilateral(self):
        self.assertEqual(classifyTriangle(3, 3, 3), 'Equilateral', '3,3,3 should be Equilateral')

    # Test Isosceles triangle: Exactly two sides are equal
    def test_isosceles(self):
        self.assertEqual(classifyTriangle(5, 5, 3), 'Isosceles', '5,5,3 should be Isosceles')

    # Test Scalene triangle: All sides are different
    def test_scalene(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Scalene', '3,4,5 should be Scalene')

    # Test Right triangle: Follows Pythagorean theorem
    def test_right_triangle(self):
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right', '5,12,13 should be a Right triangle')

    # Test Invalid triangle - sum of two sides less than or equal to the third
    def test_invalid_triangle_sum(self):
        self.assertEqual(classifyTriangle(1, 10, 12), 'NotATriangle', '1,10,12 is Not a Triangle')

    # Test Invalid triangle - negative side length
    def test_invalid_triangle_negative(self):
        self.assertEqual(classifyTriangle(-1, 4, 5), 'InvalidInput', 'Negative side length should be InvalidInput')

    # Test Invalid triangle - zero side length
    def test_invalid_triangle_zero(self):
        self.assertEqual(classifyTriangle(0, 4, 5), 'InvalidInput', 'Zero side length should be InvalidInput')

    # New Test with large values beyond valid range
    def test_large_values(self):
        self.assertEqual(classifyTriangle(1000000, 1000000, 1000000), 'InvalidInput', 'Sides too large should be InvalidInput')

    # New Test with floating-point values (invalid for integer inputs)
    def test_floating_point(self):
        self.assertEqual(classifyTriangle(0.5, 0.5, 0.5), 'InvalidInput', 'Floating-point values should be InvalidInput')

    # New Test boundary case where the sum equals the third side
    def test_boundary_values(self):
        self.assertEqual(classifyTriangle(1, 1, 2), 'NotATriangle', '1,1,2 is Not a Triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

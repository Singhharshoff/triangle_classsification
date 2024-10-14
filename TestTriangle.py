import unittest
from Triangle import classifyTriangle

class TestClassifyTriangle(unittest.TestCase):
    
    # Test Equilateral triangle
    def test_equilateral(self):
        self.assertEqual(classifyTriangle(3, 3, 3), 'Equilateral')
    
    # Test Isosceles triangle
    def test_isosceles(self):
        self.assertEqual(classifyTriangle(5, 5, 3), 'Isosceles')
    
    # Test Scalene triangle
    def test_scalene(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Scalene')

    # Test Invalid triangle - sum of two sides less than the third
    def test_invalid_triangle_sum(self):
        self.assertEqual(classifyTriangle(1, 10, 12), 'Invalid')

    # Test Invalid triangle - negative side length
    def test_invalid_triangle_negative(self):
        self.assertEqual(classifyTriangle(-1, 4, 5), 'Invalid')
    
    # Test Invalid triangle - zero side length
    def test_invalid_triangle_zero(self):
        self.assertEqual(classifyTriangle(0, 4, 5), 'Invalid')

    # New Test with large values
    def test_large_values(self):
        self.assertEqual(classifyTriangle(1000000, 1000000, 1000000), 'Equilateral')

    # New Test with floating-point values
    def test_floating_point(self):
        self.assertEqual(classifyTriangle(0.5, 0.5, 0.5), 'Equilateral')

    # New Test boundary case where the sum equals the third side
    def test_boundary_values(self):
        self.assertEqual(classifyTriangle(1, 1, 2), 'Invalid')

if __name__ == '__main__':
    unittest.main()

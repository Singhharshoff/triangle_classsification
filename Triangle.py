# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Oct 14, 2024

The primary goal of this file is to demonstrate a simple python program 
to classify triangles based on the lengths of their sides.

@author: jrr
@author: rk
"""

def classifyTriangle(a, b, c):
    """
    Classify a triangle based on the side lengths provided.

    Parameters:
    a, b, c: Side lengths of the triangle (must be positive integers <= 200).

    Returns:
        - 'Equilateral' if all sides are equal.
        - 'Isosceles' if exactly two sides are equal.
        - 'Scalene' if all sides are different.
        - 'Right' if it satisfies the Pythagorean theorem.
        - 'NotATriangle' if the inputs do not form a valid triangle.
        - 'InvalidInput' if the inputs are invalid (e.g., negative, non-integers, or > 200).
    """

    # Input validation: Check if inputs are integers within the valid range
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'
    if a <= 0 or b <= 0 or c <= 0 or a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
    
    # Check if it's a valid triangle: The sum of any two sides must be greater than the third side
    if a + b <= c or a + c <= b or b + c <= a:
        return 'NotATriangle'
    
    # Triangle classification logic
    if a == b == c:
        return 'Equilateral'
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return 'Right'
    elif a == b or b == c or a == c:
        return 'Isosceles'
    else:
        return 'Scalene'

# Triangle.py

def classifyTriangle(a, b, c):
    """
    This function classifies a triangle based on the lengths of its three sides.
    
    :param a: side a of the triangle
    :param b: side b of the triangle
    :param c: side c of the triangle
    :return: a string describing the type of triangle ('Equilateral', 'Isosceles', 'Scalene', 'Invalid')
    """
    # Check if any side length is less than or equal to zero
    if a <= 0 or b <= 0 or c <= 0:
        return 'Invalid'

    # Check if the sides do not form a valid triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return 'Invalid'

    # Determine the type of triangle
    if a == b == c:
        return 'Equilateral'
    elif a == b or b == c or a == c:
        return 'Isosceles'
    else:
        return 'Scalene'

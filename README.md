# README for Triangle Classification and Testing
## Introduction
This project demonstrates a Python program that classifies triangles based on the lengths of their three sides. It includes a unit testing suite (TestTriangle.py) to validate the correctness of the classification. The program was initially flawed, producing incorrect classifications and failing unit tests, but these issues were identified and fixed to ensure proper functionality.
## Problematic Behavior in Original Code
The original Triangle.py and TestTriangle.py files had several logic errors, which led to failures in triangle classification. The key issues identified were:
### 1. Incorrect Input Validation
The code had a faulty condition that incorrectly validated the side lengths. For example:
if a <= 0 or b <= b or c <= 0:
This condition had an error with b <= b, which is always True, making input validation incorrect.
### 2. Triangle Inequality Check
The triangle inequality theorem, which ensures the sum of any two sides is greater than the third, was incorrectly implemented as:
if (a >= (b - c)) or (b >= (a - c)) or (c >= (a + b)):
This condition doesn’t validate the triangle inequality rule correctly.
### 3. Equilateral Triangle Check
The condition for equilateral triangles incorrectly checked
if a == b and b == a:
This check doesn’t ensure all three sides are equal.
### 4. Right Triangle Check
The Pythagorean theorem check for a right triangle was incorrect and caused incorrect results for right triangles.
### 5. Other Logical Errors
There were issues in the logic for determining Scalene and Isosceles triangles, leading to incorrect classifications.
# How the Issues Were Fixed
The following changes were made to Triangle.py to address the issues:
## 1. Correct Input Validation
The input validation logic was corrected to ensure that the side lengths are valid positive integers and that no side exceeds the maximum allowed length (200):

if a > 200 or b > 200 or c > 200 or a <= 0 or b <= 0 or c <= 0:
    return 'InvalidInput'

## 2. Correct Triangle Inequality Check
The triangle inequality theorem was implemented correctly. This ensures that the sum of any two sides is greater than the third:

if (a + b <= c) or (a + c <= b) or (b + c <= a):
    return 'NotATriangle'

## 3. Correct Equilateral Triangle Check
The check for an equilateral triangle was simplified to ensure that all three sides are equal:

if a == b == c:
    return 'Equilateral'

## 4. Correct Right Triangle Check
The logic to check for a right triangle using the Pythagorean theorem was corrected:

if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
    return 'Right'

## 5. Fixing Scalene and Isosceles Logic
The logic for classifying Scalene and Isosceles triangles was corrected as follows:

if a == b or b == c or a == c:
    return 'Isosceles'
return 'Scalene'

# Running the Tests
The unit tests in TestTriangle.py validate the triangle classification logic. After applying the fixes in Triangle.py, the tests now pass successfully.

To run the tests, execute the following commands in my jupyter notebook:
<img width="959" alt="image" src="https://github.com/user-attachments/assets/21da3b51-4742-46f7-906e-615f22e73d03">
<img width="909" alt="image" src="https://github.com/user-attachments/assets/5fec6181-59e1-40c4-a55c-a8fbdc0e6052">
<img width="908" alt="image" src="https://github.com/user-attachments/assets/e1f60afc-cadb-4db4-ba0d-58fd266a4269">
<img width="893" alt="image" src="https://github.com/user-attachments/assets/2857b330-a39a-4540-a5f4-b20d50e28384">
<img width="890" alt="image" src="https://github.com/user-attachments/assets/2c342a06-48b4-4188-bf61-79fbd6abe2e1">
<img width="902" alt="image" src="https://github.com/user-attachments/assets/6674dd87-53bc-414c-8353-5a7a05e91699">
<img width="875" alt="image" src="https://github.com/user-attachments/assets/f3405e5c-55c8-4307-a5ef-dd81efe232f0">
<img width="901" alt="image" src="https://github.com/user-attachments/assets/13d1bf33-b502-4617-8ea7-b3e2182ecf7b">

# Conclusion
This project highlights the importance of unit testing and debugging in fixing logic errors in code. The original Triangle.py had issues with input validation, triangle inequality checks, and classification logic for equilateral and right triangles. After identifying and correcting these flaws, the program now accurately classifies triangles and passes all unit tests. This demonstrates the value of systematic testing in ensuring code reliability and correctness.


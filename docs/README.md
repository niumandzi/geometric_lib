# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

# Program Description

This Python program calculates and displays the perimeter or area of geometric figures, specifically circles and squares. It dynamically imports and calls functions to achieve this functionality.

# Function Descriptions

## Circle Area

This function calculates the area of a circle.

- **Parameters**: 
  - `r` (int): The radius of the circle.
- **Returns**: 
  - `float`: The area of the circle.
- **Example Call**: 
  - Given `int` 5, the function returns `float` 78.53981633974483


## Circle Perimeter

This function calculates the circumference of a circle.

- **Parameters**: 
  - `r` (int): The radius of the circle.
- **Returns**: 
  - `float`: The perimeter of the circle.
- **Example Call**: 
  - Given `int` 5, the function returns `float` 31.41592653589793

## Square Area

This function calculates the area of a square.

- **Parameters**: 
  - `a` (int): The length of the side of the square.
- **Returns**: 
  - `int`: The area of the square.
- **Example Call**:
  - Given `int` 4, the function returns `int` 16

## Square Perimeter

This function calculates the perimeter of a square.

- **Parameters**: 
  - `a` (int): The length of the side of the square.
- **Returns**: 
  - `int`: The perimeter of the square.
- **Example Call**: 
  - Given `int` 4, the function returns `int` 16

## Triangle Area

This function calculates the area of a triangle.

- **Parameters**: 
  - `a`, `b`, `c` (int): The lengths of the sides of the triangle.
- **Returns**: 
  - `float`: The area of the triangle.
- **Example Call**: 
  - Given `int` 3, 4, 5, the function returns `float` 6.0

## Triangle Perimeter

This function calculates the perimeter of a triangle.

- **Parameters**: 
  - `a`, `b`, `c` (int): The lengths of the sides of the triangle.
- **Returns**: 
  - `int`: The perimeter of the triangle.
- **Example Call**: 
  - Given `int` 3, 4, 5, the function returns `int` 12

# Project History
Here's a brief history of project changes with commit hashes:

1. **Commit 8ba9aeb**: L-03: Circle and square added
   - Added initial implementation for circle and square calculations

2. **Commit d078c8d**: L-03: Docs added
   - Added documentation for existing functionality

3. **Commit d080c78**: L-04: Triangle added
   - Implemented triangle calculations

4. **Commit 51c40eb**: L-04: Doc updated for triangle
   - Updated documentation to include triangle information

5. **Commit d76db2a**: L-04: Add calculate.py
   - Added main calculation file

6. **Commit b5b0fae**: L-04: Update docs for calculate.py
   - Updated documentation for the new calculate.py file

7. **Commit 3049431**: L-04: Add rectangle.py
   - Added rectangle calculations

8. **Commit 6adb962**: L-03: Docs added
   - Added more documentation

9. **Commit 438b89a**: L-05: Add user agreement
   - Added user agreement to the project

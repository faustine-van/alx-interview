# 0x07. Rotate 2D Matrix

Given an n x n 2D matrix, rotate it 90 degrees clockwise.

  1. Prototype: def rotate_2d_matrix(matrix):
  2. Do not return anything. The matrix must be edited in-place.
  3. You can assume the matrix will have 2 dimensions and will not be empty.
```
jessevhedden$ cat main_0.py
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

jessevhedden$
jessevhedden$ ./main_0.py
[[7, 4, 1],
[8, 5, 2],
[9, 6, 3]]
jessevhedden$
```

### Reference
- [Data Structures (list comprehensions, nested list comprehension)](https://docs.python.org/3/tutorial/datastructures.html)
- [More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Inplace rotate square matrix by 90 degrees](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
- [Transpose a matrix in Single line in Python](https://www.geeksforgeeks.org/transpose-matrix-single-line-python/)
- [Python Lists for basics of list manipulation in Python.](https://www.tutorialspoint.com/python/python_lists.htm)

#!/usr/bin/python3
"""
Defines a function def pascal_triangle(n): that returns a
list of lists of integers representing the Pascal’s triangle of n:
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the
    Pascal's triangle of n:
    (1),
    (1 1),
    (1 2 1),
    (1 3 3 1),
    ...
    """
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        triangle = pascal_triangle(n - 1)
        last_row = triangle[-1]

        new_row = [1] + [sum(x) for x in zip(last_row, last_row[1:])] + [1]

        triangle.append(new_row)

        return triangle

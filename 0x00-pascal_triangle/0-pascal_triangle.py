#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    f = []
    if n <= 0:
        return f
    f = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(f[i - 1]) - 1):
            curr = f[i - 1]
            temp.append(f[i - 1][j] + f[i - 1][j + 1])
        temp.append(1)
        f.append(temp)
    return f

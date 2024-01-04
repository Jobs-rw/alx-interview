#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns an empty list if n <= 0
    """
    result = []
    if n <= 0:
        return result
    
    # Initialize with the first row
    result = [[1]]
    
    # Loop to generate the Pascal Triangle
    i = 1
    while i < n:
        temp = [1]
        for j in range(len(result[i - 1]) - 1):
            temp.append(result[i - 1][j] + result[i - 1][j + 1])
        temp.append(1)
        result.append(temp)
        i += 1

    return result


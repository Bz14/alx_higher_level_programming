#!/usr/bin/python3
""" A module contai ing a pascal triangle function """


def pascal_triangle(n):
    """A function to define pascal triangle"""
    if n <= 0:
        return []
    ans = [[1]]
    while len(ans) != n:
        row = [1]
        last_row = ans[-1]
        for j in range(len(last_row) - 1):
            row.append(last_row[j] + last_row[j + 1])
        row.append(1)
        ans.append(row)
    return ans

#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    for row in matrix:
        res = []
        for val in row:
            res.append(val ** 2)
        newMatrix.append(res)
    return newMatrix

#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = [[0 for _ in range(len(row))] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            newMatrix[i][j] = matrix[i][j] ** 2
    return newMatrix

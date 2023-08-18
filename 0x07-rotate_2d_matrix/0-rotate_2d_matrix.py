#!/usr/bin/python3
'''3d matrix rotation function'''


def rotate_2d_matrix(matrix):
    '''2D matrix that rotates it 90 degrees clockwise'''
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

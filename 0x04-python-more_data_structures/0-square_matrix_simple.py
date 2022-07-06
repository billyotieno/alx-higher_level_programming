#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for index, array in enumerate(matrix):
        for item_index, item in enumerate(array):
            matrix[index][item_index] = item ** 2
    return matrix
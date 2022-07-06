#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for x in matrix:
        new.append(list(map(lambda x: x**2, x)))
    return (new)
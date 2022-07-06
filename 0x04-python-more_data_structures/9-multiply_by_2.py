#!/usr/bin/python3
def multiply_by_2(my_dict):
    cpy_dict = my_dict.copy()
    for x in cpy_dict.keys():
        cpy_dict[x] *= 2
    return cpy_dict

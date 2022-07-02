#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list[:]
    for idx, number in enumerate(new_list):
        if number % 2 == 0:
            new_list[idx] = True
        else:
            new_list[idx] = False
    return new_list

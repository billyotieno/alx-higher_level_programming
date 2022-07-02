#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for idx, number in enumerate(my_list):
        if number % 2 == 0:
            my_list[idx] = True
        else:
            my_list[idx] = False
    return my_list

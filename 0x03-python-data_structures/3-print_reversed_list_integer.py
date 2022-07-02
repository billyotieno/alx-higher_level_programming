#!/usr/bin/python3
def print_reversed_list_integer(mylist=[]):
    mylist.reverse()
    for number in mylist:
        print('{:d}'.format(number))

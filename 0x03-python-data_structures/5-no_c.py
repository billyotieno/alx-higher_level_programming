#!/usr/bin/python3
def no_c(my_string):
    my_string.upper()
    if 'C' in my_string:
        my_string_ls = list(my_string)
        my_string_ls.remove('C')
        return "".join(my_string_ls)
    elif 'c' in my_string:
        my_string_ls = list(my_string)
        my_string_ls.remove('c')
        return "".join(my_string_ls)
    else:
        return my_string

#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == None or len(my_list) == 0:
        return None
    big = my_list[0]
    for i in range(len(my_list)):
        if big < my_list:
            big = my_list[i]
    return big

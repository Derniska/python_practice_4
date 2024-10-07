# This module finds two smallest numbers in a list
def find_two_smallest(my_list):
    sorted_list = sorted(my_list, reverse = False)[:2]
    if sorted_list[0] == sorted_list[1]:
        sorted_list.pop(0)
    return sorted_list
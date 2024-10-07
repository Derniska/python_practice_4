# This module creates lists (number of list is defined by the user from a prompt)
import random
random.seed(42)
def get_lists():
    n = int(input('How many lists do you need? '))
    q = int(input('How many integers do you want there to be in each list? '))
    my_list = {}
    for i in range(n):
        my_list[f'list_{i+1}'] = random.sample(range(100), k = q)
    return my_list
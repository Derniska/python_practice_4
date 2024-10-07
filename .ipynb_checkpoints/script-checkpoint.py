import module_1 as m1
import module_2 as m2

def get_two_smallest(my_dict):
    variables = {}
    for i,key in enumerate(my_dict.keys()):
        variables[f'list_{i+1}'] = m1.find_two_smallest(my_dict[key])
    return variables
my_list = m2.get_lists()
nums = get_two_smallest(my_list)
with open('result.txt', 'w') as file:
    for key in nums.keys():
        file.write(f'The smallest numbers in the {key} are {nums[key]}\n')

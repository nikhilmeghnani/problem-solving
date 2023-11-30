# output: [150, 200, 300]
my_map = {'a': 150,'b': 75,'c': 200, 'd': 50, 'e': 300}

def value_greater_than_given(my_map):
    output_list = []
    for key, value in my_map.items():
        if value > 100:
            output_list.append(value)
    return output_list

print(value_greater_than_given(my_map))
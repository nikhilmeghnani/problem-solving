# output: {1: 2, 2: 2, 3: 1, 4: 2, 5: 1, 6: 1}
input_data = [1,2,3,4,5,1,2,4,6]

def count_element_in_list(data_list):
    result_dict = {}
    for item in data_list:
        result_dict[item] = result_dict.get(item, 0)+1
    return result_dict

print(count_element_in_list(input_data))
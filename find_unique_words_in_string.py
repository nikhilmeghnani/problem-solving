# input_str = "nikhil is is a data engineer"
# output: ['nikhil', 'a', 'data', 'engineer']
input_str = "nikhil is is a data engineer"

def find_unique_words(input_str):
    dict = {}
    output_list = []
    for item in input_str.split():
        if item not in dict:
            dict[item] = 1
        else:
            dict[item] = dict[item] + 1

    for key, value in dict.items():
        if value == 1:
            output_list.append(key)
    return output_list

print(find_unique_words(input_str))
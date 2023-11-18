def even_num_square(num_list):
    output_list = []
    for each in num_list:
        if each%2==0:
            square_num = int(each * each)
            output_list.append(square_num)
    return output_list

num_list = [1,2,3,4,5,6,7]
square_num_list = even_num_square(num_list)
print(square_num_list)
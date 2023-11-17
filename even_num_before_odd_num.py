#
# def welcome(name):
#     print(f"welcome {name} to kia")
#
# fruit_list = ['apple', 'mango', 'banana', 'kanda']
#
# def print_fruits(fruit_list):
#     # for fruit in fruit_list:
#     #     print(fruit)
#
#     [print(fruit) for fruit in fruit_list]
# if __name__ == '__main__':
#     # print("mukesh")
#     # get_name = input("enter username: ")
#     get_name = 'nikhil'
#     welcome(get_name)
#     print_fruits(fruit_list)
input_list = [1,2,3,4,5,6,7,10,12,14,17,19,20]
def get_event(input_list):
    output_list = []
    for each in range(len(input_list)-1):
        if(input_list[each]%2 == 0 and input_list[each+1]%2 == 1):
            # print(input_list[each])
            output_list.append(input_list[each])
    return output_list
print(get_event(input_list))

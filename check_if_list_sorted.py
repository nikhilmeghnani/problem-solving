# input:
# output: False


def is_list_sorted(num_list):
    k = 0
    for num in range(len(num_list)-1):
        if (num_list[num] <= num_list[num+1]):
            pass
        else:
            k = 1
            break
    return k==0

l1 = [1,2,3,4,5]
l2 = [1,5,2,3,4,5,1]
print(is_list_sorted(l2))

def is_list_sorted(num_list):
    return all((num_list[num] <= num_list[num+1]) for num in range(len(num_list)-1))

print(is_list_sorted(l2))

num_list = [1,2,3,4,5,1,2]
# {1: 2, 2: 2, 3: 1, 4: 1, 5: 1}

def count_freq(num_list):
    freq = {}
    for num in num_list:
        if num in freq:
            freq[num] = freq[num] + 1
        else:
            freq[num] = 1
    return freq

print(count_freq(num_list))

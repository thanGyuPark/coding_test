def solution(array):
    freq = {}
    for i in array:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    max_count_num = max(freq.values())
    
    check = [k for k, v in freq.items() if v == max_count_num]
    
    if len(check) > 1:
        return -1
    else:
        return check[0]
    
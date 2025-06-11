def solution(my_string, n):
    result = ''
    for ch in my_string:
        result += ch * n
    return result
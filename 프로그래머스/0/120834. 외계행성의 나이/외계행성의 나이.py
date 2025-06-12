def solution(age):
    digit_to_char = ['a','b','c','d','e','f','g','h','i','j']
    answer = ''
    for i in str(age):
        answer += digit_to_char[int(i)]
    return answer
def solution(n):
    answer = 0
    for a in range(1, int(n**0.5) + 1):
        if n % a == 0:
            b = n // a
            if a == b:
                answer += 1
            else:
                answer += 2
    return answer
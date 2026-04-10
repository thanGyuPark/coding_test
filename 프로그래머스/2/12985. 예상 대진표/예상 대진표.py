import math

def solution(n,a,b):
    count = 1
    while True:
        if(abs(a-b)==1 and min(a,b)%2==1): break
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        count += 1
    return count

# N명이 참가하고 토너먼트 형식으로 진행
# N-1 <-> N 참가자끼리 게임을 진행
# 각 게임에서 이긴 사람은 다음 라운드 진출
# 다음 라운드 진출할 참가자 번호는 1~N/2번을 차례로 배정
# 최종 한 명 남을때까지 진행
# 처음 라운드에서 A번을 가진 참가자는 경쟁자로 생각하는 B번 참가자와 몇 번째 라운드에서 만나는가?

# A번과 B번을 가진 참가자는 라운드가 진행될때마다 N/2번으로 변화
# A+1=B이거나 B+1=A인 경우까지 count 증가
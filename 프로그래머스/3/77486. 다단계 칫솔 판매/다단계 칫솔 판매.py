import math
from collections import defaultdict

def solution(enroll, referral, seller, amount):
    parent_dict = {}
    for i,r in enumerate(referral):
        parent_dict[enroll[i]] = r
    
    money_dict = defaultdict(int)
    
    for i,s in enumerate(seller):
        a = amount[i] * 100
        me = s
        while True:
            if me=='-': break
            p_money = math.floor(a/10)
            if p_money<1: 
                money_dict[me] += a
                break
            my_money = a-p_money
            parent = parent_dict[me]
            money_dict[me] += my_money
            me = parent
            a = p_money
            
    result = []
    for e in enroll:
        result.append(money_dict[e])
    return result
        

# 이익 분배는 10%를 추천인이게 배분하고 나머지는 자신이 가진다
# 모든 판매원은 자신이 판매한 칫솔과 가입시킨 판매원의 10%
# 자신에게 발생하는 이익도 부모에게 줘야 함
# 판매원에게 배분된 이익금의 총합을 반환

# referral이 -라면 부모는 center
# 아니라면 해당 인원이 부모
# 나:부모 의 dict를 생성
# 부모가 -가 되거나 이익금의 10%가 1보다 작을 경우 정지

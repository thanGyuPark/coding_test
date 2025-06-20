def solution(numer1, denom1, numer2, denom2):
    up = (numer1*denom2) + (numer2*denom1)
    down = (denom1 * denom2)
    
     # 최대공약수로 기약분수로 만들기
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    common = gcd(up, down)
    return [up // common, down // common]
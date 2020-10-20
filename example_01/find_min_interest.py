# (원금 p, 목표금액 d, 개월 m, 월 이율 k)
# P, d, m 이 배열로 주어질 때 k를 구하라. 단, k는 %단위에서 *1000곱한 후 소수점은 반올림

arr = list(map(int, input().split(' ')))
p = arr[0]
d = arr[1]
m = arr[2]
# k는 이자(%)에 1000을 곱한 후 소수점 첫째자리에서 반올림한 수

def solveInterest(p, d, m):
    numPercent = 100 # %트 변환을 위한 가중치
    numMultiVal = 1000 # 1000을 곱한 수로 반환하기 위한 가중
    numRoundVal = 10 # 소수점 첫째짜리에서 반올림하기 위한 가중

    for i in range(1*numPercent*numMultiVal*numRoundVal): # 1은 이자 100%를 의미. 즉 이자가 0%에서 100%까 0.000001% 씩 증가
        k = i / (numPercent*numMultiVal*numRoundVal) # 이자 계산을 위한 수로 변환지 4.1% => 0.041
        if p*(1+k)**m >= d:
            ans = round(i/numRoundVal)
            print(i, ans)
            return(ans)
            break

solveInterest(p, d, m)

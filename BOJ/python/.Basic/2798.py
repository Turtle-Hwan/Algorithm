#2798번 블랙잭
'''
from itertools import combinations

N, M = map(int, input().split())

cardNum = list(map(int, input().split()))

cardNumCombi = list(map(list, combinations(cardNum, 3)))

answer = 0

for i in range(len(cardNumCombi)):
    if((sum(cardNumCombi[i]) <= M) and (answer < sum(cardNumCombi[i]))):
        answer = sum(cardNumCombi[i])

print(answer)
'''
#내장 함수 안 쓰고

N, M = map(int, input().split())

cardNum = list(map(int, input().split()))

for i in range(

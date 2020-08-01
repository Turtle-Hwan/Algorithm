#2750번 수 정렬하기

import sys
input = sys.stdin.readline

N = int(input())

num = list()

for i in range(N):
    num.append(int(input()))

num.sort()

[print(i) for i in num]

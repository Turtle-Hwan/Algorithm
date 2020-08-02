#1920번 수 찾기

'''이분탐색'''

import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

M = int(input())

num = list(map(int, input().split()))

A.sort()

answer = list()

for i in range(M):
    if(num[i] < A[0] or num[i] > A[N-1]):
        answer.append(0)
    else:
        if(num[i] in A):
            answer.append(1)
        else:
            answer.append(0)

[print(i) for i in answer]

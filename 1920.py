#1920번 수 찾기

'''이분탐색: 주어진 배열의 중앙값을 기준으로 찾는 값이 포함되는 부분만 계속 절반으로 나누어 가는 방법'''

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
        B = A
        while(True):
            m = len(B)//2
            if(num[i] == B[m]):
                answer.append(1)
                break
            elif(num[i] > B[m]):
                B = list(filter(lambda x: x > A[m], A))
            elif(num[i] < B[m]):
                B = list(filter(lambda x: x < A[m], A))
        
[print(i) for i in answer]

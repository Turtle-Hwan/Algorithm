#1920번 수 찾기

'''이분탐색(이진 탐색): 주어진 배열의 중앙값을 기준으로 찾는 값이 포함되는 부분만 계속 절반으로 나누어 가는 방법'''

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
        end = N-1
        start = 0
        
        while(True):
            m = (start+end)//2
            if(start == end and num[i] != B[m]):
                answer.append(0)
                break
            elif(num[i] == B[m]):
                answer.append(1)
                break
            elif(num[i] > B[m]):
                start = m+1
            elif(num[i] < B[m]):
                end = m-1
            
[print(i) for i in answer]

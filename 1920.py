#1920번 수 찾기

'''이분탐색(이진 탐색): 주어진 배열의 중앙값을 기준으로 찾는 값이 포함되는 부분만 계속 절반으로 나누어 가는 방법'''

import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

M = int(input())

num = list(map(int, input().split()))

A.sort()

for i in range(M):
    end = N-1
    start = 0
        
    while(start <= end):
        m = (start+end)//2
        if(num[i] == A[m]):
            print(1)
            break
        elif(num[i] > A[m]):
            start = m+1
        elif(num[i] < A[m]):
            end = m-1
            
    if(num[i] != A[m]):
        print(0)


#set() 자료형 이용 (x in set() --> O(1))

'''
import sys
input = sys.stdin.readline

N = int(input())

A = set(input().split())

M = int(input())

num = input().split()

for i in range(M):
    if(num[i] in A):
        print(1)
    else:
        print(0)
'''

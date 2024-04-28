# 11003번 최솟값 찾기 플5
'''
* 이동하는 구간에 대한 최솟값 구하기

1. 우선순위 큐와 힙을 이용한 구간 정렬하면서 나아가기?

2. 세그먼트 트리로 구간 최소값 구하기
'''

import sys

N, L = map(int, input().split())
Alist = list(map(int, sys.stdin.readline().split()))
Dlist = list()

print(N, L, Alist)

min_num = Alist[0]
Dlist.append(min_num)

for i in range(0, N):
    print(i - L + 1, i)

'''
12 3
1 5 2 3 6 2 3 7 3 5 2 6
'''
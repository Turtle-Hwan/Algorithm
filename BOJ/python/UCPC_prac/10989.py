# 수 정렬하기 3 -> 도수정렬 counting sort 사용!

import sys
input = sys.stdin.readline

N = int(input())

list_num = [0] * 10001

for _ in range(N):
  list_num[int(input())] += 1

for i in range(len(list_num)):
  while(list_num[i] > 0):
    print(i)
    list_num[i] -= 1

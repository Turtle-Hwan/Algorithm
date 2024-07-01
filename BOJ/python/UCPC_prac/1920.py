# 수 찾기 / 이분탐색 // set으로 바꾸면 hash이므로 in을 써도 속도가 빠르다.

import bisect

N = int(input())
N_list = list(map(int, input().split()))
N_list.sort()

M = int(input())
M_list = list(map(int, input().split()))

for i in M_list:
  if bisect.bisect_left(N_list, i) == N:
    print(0)
  elif N_list[bisect.bisect_left(N_list, i)] == i:
    print(1)
  else:
    print(0)
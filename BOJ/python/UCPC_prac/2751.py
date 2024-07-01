# 24.07.01 수 정렬하기 2
import sys
input = sys.stdin.readline

N = int(input())

list_N = list()
for _ in range(N):
  list_N.append(int(input()))

list_N.sort()

print(*list_N)
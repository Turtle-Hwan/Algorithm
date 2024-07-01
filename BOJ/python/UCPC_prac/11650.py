# 좌표 정렬하기

N = int(input())

list_coord = list()

for _ in range(N):
  list_coord.append(list(map(int, input().split())))

[print (*x) for x in sorted(list_coord)]

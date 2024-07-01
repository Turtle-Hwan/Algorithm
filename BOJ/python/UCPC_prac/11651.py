# 좌표 정렬하기 2 / 2차원 정렬 역순

N = int(input())

list_coord = list()

for _ in range(N):
  list_coord.append(list(map(int, input().split())))

[print (*x) for x in sorted(list_coord, key=lambda x: (x[1], x[0]))]

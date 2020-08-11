#11651번 좌표 정렬하기 2

import sys
input = sys.stdin.readline

N = int(input())

coordinate = list()

for i in range(N):
    coordinate.insert(i, list(map(int, input().split())))

a = sorted(coordinate, key=lambda coordinate: coordinate[0])
b = sorted(a, key=lambda a: a[1])

[print(b[i][0], b[i][1]) for i in range(N)]

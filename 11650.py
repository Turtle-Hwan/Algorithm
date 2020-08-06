#11650번 좌표 정렬하기

import sys
input = sys.stdin.readline

N = int(input())

coordinate = list()

for i in range(N):
    coordinate.insert(i, list(map(int, input().split())))

a = sorted(coordinate, key = lambda coordinate: coordinate[1])
b = sorted(a, key = lambda a: a[0])

[print(b[i][0], b[i][1]) for i in range(len(b))]

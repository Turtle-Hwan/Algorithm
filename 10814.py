#10814번 나이순 정렬

from sys import stdin
input = stdin.readline

N = int(input())

member = list()

for i in range(N):
    member.insert(i, list(input().split()))

a = sorted(member, key = lambda member: int(member[0]))

[print(a[i][0], a[i][1]) for i in range(N)]

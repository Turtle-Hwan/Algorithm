#15552번 빠른 A+B

import sys

def input():
    return sys.stdin.readline()

T = int(input())

answer = list()

for i in range(T):
    A, B = map(int, input().split())
    answer.append(A + B)

for i in range(T):
    print(answer[i])

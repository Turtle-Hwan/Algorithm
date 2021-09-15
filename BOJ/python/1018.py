#1018번 체스판 다시 칠하기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = list()

for i in range(N):
    a = input().rstrip()
    board.append([])
    for j in range(M):
        board[i].append(a[j])

'''나올 수 있는 보드의 두 가지 경우와 일일히 비교'''

BW = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
WB = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']

b1 = [BW, WB, BW, WB, BW, WB, BW, WB]
b2 = [WB, BW, WB, BW, WB, BW, WB, BW]

answer1, answer2 = 100, 100

for y in range(N-7):
    for x in range(M-7):
        change1, change2 = 0, 0
        for i in range(8):
            for j in range(8):
                if(board[i+y][j+x] != b1[i][j]):
                    change1 += 1
                if(board[i+y][j+x] != b2[i][j]):
                    change2 += 1

        if(answer1 > change1):
            answer1 = change1
        if(answer2 > change2):
            answer2 = change2


if(answer1 >= answer2):
    print(answer2)
else:
    print(answer1)

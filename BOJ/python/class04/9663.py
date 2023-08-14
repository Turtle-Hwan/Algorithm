# 9663번 N-Queen
# pypy로 제출 시에만 시간 초과 안남..

N = int(input())

queen_list = [-1 for i in range(N)]     # queen_list[x] = y  -> x 행에 y번째 열에 퀸이 놓여있다는 뜻

count = [0]
def recurs_queen(queen_list : list[int], x : int, count):  #x + 1 행 탐색 , y 0~n 탐색
    if x >= N:
        count[0] += 1
        return

    for y in range(0, N):
        if x == 0:
            queen_list[x] = y
            recurs_queen(queen_list, x + 1, count)
        else:
            is_pos = 1
            for i in range(0, x):
                if (queen_list[i] == y) or (x + y == i + queen_list[i]) or (x - y == i - queen_list[i]):
                    is_pos = 0
                    break
            if is_pos == 1:
                queen_list[x] = y
                recurs_queen(queen_list, x + 1, count)

recurs_queen(queen_list, 0, count)

print(*count)
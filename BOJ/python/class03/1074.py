#1074번 Z
'''
분할 정복.
각 칸에 탐색 순번 넣기. 

[x][y]
[x+1][y]
[x][y+1]
[x+1][y+1]

메모리 초과... 배열 만들지 않고 해결하기
'''
'''
def Zsearch(array, N, x, y, s, r, c):    #기본 배열, 배열 크기 2**N, 배열 좌표, 시작 번호
    if N == 1:
        #z모양 방문 후 번호 붙임 (s부터 번호 시작)
        array[y][x] = s
        array[y][x+1] = s+1
        array[y+1][x] = s+2
        array[y+1][x+1] = s+3
    else:
        Zsearch(array, N-1, x, y, s)
        Zsearch(array, N-1, x + 2**(N-1), y, s + 4**(N-1))
        Zsearch(array, N-1, x, y + 2**(N-1), s + 2*4**(N-1))
        Zsearch(array, N-1, x + 2**(N-1), y + 2**(N-1), s + 3*4**(N-1))
'''        
   

def Zsearch(N, s, r, c):    #기본 배열, 배열 크기 2**N, 배열 좌표, 시작 번호
    if N == 1:
        #z모양 방문 후 번호 붙임 (s부터 번호 시작)
        a = [[0, 0], [0, 0]]
        a[0][0] = s
        a[0][1] = s+1
        a[1][0] = s+2
        a[1][1] = s+3
        #print(r, c, s)
        return a[r][c]
    else:
        # 사분면 중 하나 선택해서 축소
        #0 1       c: 0~2^N-1 2^n-1~2^n      c//2^n-1 +  r//2^n-1    
        #         r                           0 / 1     0*2 /  1*2
        #        0~2^n-1
        #        2^n-1~2^n
        #2 3
        # r//pow(2, N-1) + 2*(c//pow(2, N-1)) >> 사분면 번호(0123)
        
        return Zsearch(N-1, s + (c//pow(2, N-1) + 2*(r//pow(2, N-1)))*4**(N-1), r%pow(2, N-1), c%pow(2, N-1))


N, r, c = map(int, input().split())
#baseArray = [[0]*pow(2, N) for _ in range(0, pow(2, N))]

ans = Zsearch(N, 0, r, c)

print(ans)
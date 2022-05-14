#2630번 색종이 만들기
'''
분할 정복.
2차원 배열에서 압축하기 문제(종만북 예제)와도 비슷한 듯.

>> x + n, y + n     n/2    0 1 2 3 4
'''

'''def division(x, y, n, 변 길이):    x, y 시작 좌표/ n : 탐색 사각형 크기
    if 탐색하다가 다른 숫자 나오면:
        분할하기
    else:
        종이 한장으로 계산.


**재귀함수 return 값 이용..?
return 값으로 하양, 파랑 종이 개수 list로 받아서 넘기고넘기기???? 
=>> 전역 변수로 두고 함수에서 바로 접근.
'''


def division(x, y, n, paper):    
    diff = paper[x][y]
    
    if n != 1:
        for a in range(x, x+n):
            for b in range(y, y+n):
                if diff != paper[a][b]:
                    nn = int(n/2)
                    division(x, y, nn, paper)
                    division(x+nn, y, nn, paper)
                    division(x, y+nn, nn, paper)
                    division(x+nn, y+nn, nn, paper)
                    return
    if diff == 0: #하양
        answer[0] += 1
    else: #파랑
        answer[1] += 1
        


N = int(input())
paper = [[0]*N for _ in range(0, N)]
answer = [0, 0]
for y in range(0, N):
    tempL = list(map(int, input().split()))
    for x in range(0, N):
        paper[y][x] = tempL[x]

division(0, 0, N, paper)
#print(paper)
print(answer[0])
print(answer[1])
        

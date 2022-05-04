#1012번 유기농 배추
'''
DFS, BFS, 그래프 탐색

DFS로 짜봐야징
왕 20분밖에 안걸렸네


>>> 중복되는 부분(while문 안의 상하좌우 탐색 조건문들)은 함수로 빼면 더 깔끔.
*** 참고
def dfs(x,y):
    if 0 <= x < n and 0 <= y < m:
        if g[x][y] == 1:
            g[x][y] = 0
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
            return 1
    return 0
    
    for i in range(n):
        for j in range(m):
            if dfs(i,j) == 1:
                count += 1
'''
    
T = int(input())
answerList = []

for _ in range(0, T):
    M, N, K = map(int, input().split()) #배추밭 가로길이 M, 세로길이 N, 배추 심어진 위치 개수 K
    cabbage = [[0]*(M+2) for _ in range(0, N+2)]

    for i in range(0, K):
        X, Y = map(int, input().split())
        cabbage[Y+1][X+1] = 1
        
    
    #print()
    #[print(width) for width in cabbage]
    
    # 배추지렁이 탐색부분 // 주변을 다 0으로 감싸면 list index 신경 안써도 될듯.
    cabbageEarthworm = 0
    isSearch = [[0]*(M+2) for _ in range(0, N+2)]
    for y in range(1, N+1):
        for x in range(1, M+1):
            stack = []
            if cabbage[y][x] == 1 and isSearch[y][x] != 1:
                isSearch[y][x] = 1
                stack.append([y, x])
                #상하좌우 탐색, isSearch 1로 바꿔놓기
                while len(stack) != 0:
                    coor = stack.pop()
                    if cabbage[coor[0]+1][coor[1]] == 1 and isSearch[coor[0]+1][coor[1]] != 1:
                        isSearch[coor[0]+1][coor[1]] = 1
                        stack.append([coor[0]+1, coor[1]])
                        
                    if cabbage[coor[0]-1][coor[1]] == 1 and isSearch[coor[0]-1][coor[1]] != 1:
                        isSearch[coor[0]-1][coor[1]] = 1
                        stack.append([coor[0]-1, coor[1]])
                        
                    if cabbage[coor[0]][coor[1]+1] == 1 and isSearch[coor[0]][coor[1]+1] != 1:
                        isSearch[coor[0]][coor[1]+1] = 1
                        stack.append([coor[0], coor[1]+1])
                        
                    if cabbage[coor[0]][coor[1]-1] == 1 and isSearch[coor[0]][coor[1]-1] != 1:
                        isSearch[coor[0]][coor[1]-1] = 1
                        stack.append([coor[0], coor[1]-1])
                
                cabbageEarthworm += 1
            
            
    answerList.append(cabbageEarthworm)    
    
[print(i) for i in answerList]
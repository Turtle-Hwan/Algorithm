# 2606번 바이러스
'''
실3  ||  20~30분?

주어진 그래프에서 연결된 노드 개수 알아내기

2차원 배열로 그래프 표시 + 탐색한 곳 표시할 배열
list queue로 활용해서 bfs 재귀로 돌림.
'''

comNum = int(input())
edgeNum = int(input())

comGraph = [[0]*(comNum+1) for _ in range(0, comNum+1)]

isSearch = [0] * comNum
isSearch[0] = 1
ans_virus = 0

for i in range(0, edgeNum):
    x, y = map(int, input().split())
    comGraph[x][y] = 1
    comGraph[y][x] = 1


def Search(startList, comGraph):
    global ans_virus
    searchList = startList
    if isSearch == [1] * comNum or len(searchList) == 0:  # 반복 끝낼 초기 조건 (모두 탐색 시 종료)
        return
    for y in range(1, comNum + 1):
        if comGraph[startList[0]][y] == 1 and isSearch[y-1] != 1: #바이러스 걸림.
            ans_virus += 1
            searchList.append(y)
            isSearch[y-1] = 1
        #else:
    del searchList[0]
    Search(searchList, comGraph)
            
Search([1], comGraph)

print(ans_virus)
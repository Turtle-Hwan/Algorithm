#11724번 연결 요소의 개수
'''
방향 없는 그래프 주어짐. 연결된 집합 개수

2차원 list에 그래프 저장.

BFS or DFS 돌리면서 개수 알아내기. 방문한 노드는 따로 저장.

RecursionError..
>> sys.setrecursionlimit 추가 / sys.stdin.readline 추가

틀림..
https://www.acmicpc.net/board/view/68534
간선 정보가 없는 노드도 연결 요소로 포함!!

6 2
3 4
4 2
답 : 4
'''

def DFS(N, stack, visit, graph):
    if len(stack) == 0:
        return
    now = stack.pop()
    for i in range(1, N+1):
        if visit[i] == 0 and graph[now][i] == 1:
            stack.append(i)
            visit[i] = 1
    DFS(N, stack, visit, graph)
                
   

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0]*(N+1) for _ in range(0, N+1)]
visit = [0]*(N+1)
for _ in range(0, M):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1
    
stack = []
ansNum = 0
for i in range(1, N+1):
    if visit[i] == 0 and len(stack) == 0:
        for j in range(1, N+1):
            if graph[i][j] == 1 and visit[i] == 0:
                stack.append(i)
                visit[i] = 1
                ansNum += 1
                #print(stack, i, j)
                #print(visit)
                DFS(N, stack, visit, graph)

#간선 정보 없는 단일 노드 더하기
for i in range(1, N+1):
    if visit[i] == 0:
        ansNum += 1
print(ansNum)
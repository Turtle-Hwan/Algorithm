#7576번 토마토
'''
하루 지나면 상하좌우 칸 토마토 익음.
며칠 지나면 다 익는지. 최소 일수

BFS의 depth 구하기

BFS 시작 노드가 두 개 있을 때 만나는 지점, depth 등을 어떻게 효율적으로 판단하는지?
>> 양쪽 1에서 둘다 돌리기에는 O(AttributeErrorN)..
>>>> 그래도 매 날짜마다 전체 순회하면서, 1인 경우 BFS로 1 퍼트리기. 하면 될 듯?

python list 얕은 복사 + 원본 객체와의 연결 주의!!!
https://crackerjacks.tistory.com/14


###
***시간초과***....
시간 흐름 1씩 시뮬 대신 bfs로 최단거리..?

>> while 안에서 전체 순회 말고, 1인 것만 찾아서 큐에 넣어놓고 돌리기.
큐 잘 사용하자..!!
'''



def BFS(x, y, Map, zeroNum):
    if Map[y][x-1] == 0:
        tomatoMap[y][x-1] = 1
        zeroNum -= 1
        newQueue.append([x-1, y])
    if Map[y][x+1] == 0:
        tomatoMap[y][x+1] = 1
        zeroNum -= 1
        newQueue.append([x+1, y])
    if Map[y-1][x] == 0:
        tomatoMap[y-1][x] = 1
        zeroNum -= 1
        newQueue.append([x, y-1])
    if Map[y+1][x] == 0:
        tomatoMap[y+1][x] = 1
        zeroNum -= 1
        newQueue.append([x, y+1])
    return zeroNum

    
import sys
from collections import deque

M, N = map(int, sys.stdin.readline().rstrip().split())
tomatoMap = [[-1]*(M+2) for _ in range(0, N+2)]    #편의를 위해 주변에 -1 벽 세워주기

visitQueue = deque()    #1 있는 [x,y]
for i in range(0, N):
    tomatoList = list(map(int, sys.stdin.readline().rstrip().split()))
    #tomatoMap[i+1][1:1+M] = tomatoList
    for j in range(1, len(tomatoList)+1):
        tomatoMap[i+1][j] = tomatoList[j-1]
        if tomatoList[j-1] == 1:
            visitQueue.append([j,i+1])
            
#[print(i) for i in tomatoMap]

zeroNum = 0
for y in range(1, N+1):
    for x in range(1, M+1):
        if tomatoMap[y][x] == 0:
            zeroNum += 1
if zeroNum == 0:    #처음부터 다 익은 경우
    print(0)
else:
    day = 0
    visitMap = [[-1]*(M+2) for _ in range(0, N+2)]    #BFS 방문처리 위함. -1 : 방문x 0: 방문0

    while True:    # 다 익을 때까지 loop 돌리기.
        #tempMap = __import__('copy').deepcopy(tomatoMap)  
        prevZeroNum = zeroNum
        # 1일에 1 루프 // 1루프당 bfs 한 사이클 => visitQueue를 다 비울때까지 loop and 새로 다 받기.
        #print(*visitQueue)
        newQueue = deque()
        while len(visitQueue) != 0:
            x, y = visitQueue.popleft()
            zeroNum = BFS(x, y, tomatoMap, zeroNum)
        visitQueue += newQueue
        #print(*visitQueue)
        #print(prevZeroNum, zeroNum)
        
        day += 1
        if zeroNum == 0 or prevZeroNum == zeroNum: #prevTomatoMap == tomatoMap:    # 정지 조건 0이 사라지거나, 0 개수가 멈춰 있거나.
            if zeroNum != 0:     #마지막에 익지 못하는 경우
                print(-1)
                break
            else:
                print(day)
                break
            
#[print(i) for i in tomatoMap]

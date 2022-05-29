#7662번 이중 우선순위 큐
'''
#아이디어 1: deque[N] 에다 오름차순 정렬 유지하는 방법
I a 가 
    if deque[0] 보다 작음. : deque.appendleft()
    elif deque[N] 보다 큼 : deque.append()
    else:
        if deque[N/2] 보다 작거나 큼: 사이에 삽입 후 나머지 밀어서 이동.
        
    최대 시간 복잡 : O(N/2 + logN) ; 최대로 미는 개수 + 이진 탐색으로 찾는 시간

D 1 : deque.pop()        O(1)
D -1 : deque.popleft()    O(1)


===
# 아이디어 2: 기존 heap + 제일 아래 노드들만 대소비교해서 빼는 방식
대소비교할 노드들 : 2*height = 2logN
대소비교에 NlogN 걸림.

대충 logN??


=======
<<<<질문 검색 + Tip>>>>
모든 연산이 O(log n) 만에 이루어져야 함.

최소-최대 힙이라게 있다.. sorted multiset 이용해도 된다.
https://en.wikipedia.org/wiki/Min-max_heap

우선순위 큐 4개로 구현?
https://www.acmicpc.net/board/view/47327
'''

#아이디어 1 구현하다 이진 탐색 머리아파서 중지..
'''
def bSearch(List, n):    #List 에서 n이 들어있는 index 반환 / 없으면 n을 넣어야 할 index 반환.
    L = 0
    R = len(List)-1
    while True:
        if L > R:
            break
        m = (R - L) // 2
        if List[m] == n:
            return m
        elif List[m] < n and List[m+1] > n:
            return m+1
        elif 
            
        if List[m] <= n: #중간값 보다 n이 큰 경우 => 오른쪽으로 이동
            L = m + 1
        else:
            R = m - 1
    return m

def doublePQ(char, n):
    if char == 'I': #삽입
        if n < DPQ[0]:
            DPQ.appendleft(n)
        elif n > DPQ[len(DPQ)-1]:
            DPQ.append(n)
        else:        
            index = bSearch(list(DPQ), n)
            print(index)
            DPQ = deque(list(DPQ)[:index] + [n] + list(DPQ)[index:])    #시간복잡도..?
        return
    elif char == 'D':  #삭제
        if len(DPQ) == 0:
            return
        elif n == 1:
            return DPQ.pop()
        elif n == -1:
            return DPQ.popleft()

import sys
input = sys.stdin.readline
from collections import deque


ans = []
T = int(input())
for _ in range(0, T):
    k = int(input())
    DPQ = deque([])
    for _ in range(0, k):
        c, n = input().split()
        n = int(n)
        doublePQ(c, n)
    
    if len(DPQ) == 0:
        ans.append('EMPTY')
    elif len(DPQ) == 1:
        ans.append(f"{DPQ[0]} {DPQ[0]}")
    else:
        ans.append(f"{DPQ[len(DPQ)-1]} {DPQ[0]}")
'''


###############################################
'''
<아이디어 3 // 풀이 아이디어>
minHeap / MaxHeap 모두 보유
둘 다 insert, 최대최소는 각각 따로 삭제 (insert O(2logN) / delete O(logN + ..?))
동기화는 안 하고, 총 노드 개수(totalN)만 따로 저장. (삭제 시 -1, 삽입 시 +1)
>> 이럴 경우, 동기화 안 되어 있어서 탐색한 노드 저장할 곳 필요.
    dict() 으로 삽입된 개수 저장 / 삭제할 때 확인하고 삭제.

if totalN == 0:
    delete 안됨.

마지막 출력 시.
if totalN >= 2:
    minH.pop()
    MaxH.pop()
elif totalN == 1:
    minH.pop()
    minH.pop()
elif totalN == 0:
    empty

'''

def doublePQ(char, n, totalN):
    if char == 'I': #삽입
        if visitD.get(n) == None:
            visitD[n] = 1
        else:
            visitD[n] += 1
            
        heapq.heappush(minHeap, n)
        heapq.heappush(maxHeap, (-n, n))
        totalN += 1
        return [totalN, None]
    elif char == 'D':  #삭제
        if totalN != 0:
            if n == 1: #최댓값 삭제
                while True:   
                    #print(totalN)
                    #print(f"maxHeap {maxHeap}")
                    #print(heapq.heappop(maxHeap))
                    
                    delN = heapq.heappop(maxHeap)[1]
                    #print(delN, visitD[delN])
                    if visitD[delN] != 0:
                        visitD[delN] -= 1
                        totalN -= 1
                        return [totalN, delN]
                        #break
                       
            elif n == -1: #최솟값 삭제
                while True:
                    delN = heapq.heappop(minHeap)
                    if visitD[delN] != 0:
                        visitD[delN] -= 1
                        totalN -= 1
                        return [totalN, delN]
                        #break
        return [totalN, None]
    

import sys
input = sys.stdin.readline
import heapq

ans = []
T = int(input())
for _ in range(0, T):
    k = int(input())
    minHeap = []
    maxHeap = []
    visitD = {}
    totalN = 0
    for _ in range(0, k):
        c, n = input().split()
        n = int(n)
        totalN = doublePQ(c, n, totalN)[0]
    if totalN >= 2:
        ans.append(f"{doublePQ('D', 1, totalN)[1]} {doublePQ('D', -1, totalN)[1]}")
    elif totalN == 1:
        oneN = doublePQ('D', 1, totalN)[1]
        ans.append(f"{oneN} {oneN}")
    elif totalN == 0:
        ans.append('EMPTY')
    
[print(i) for i in ans]
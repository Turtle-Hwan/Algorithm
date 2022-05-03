# 13913번 숨바꼭질4
'''
BFS + 경로 출력

BFS 큐에 경로까지 저장해버릴까..?
***
시간초과
>> 목적지가 더 작은 경우는 BFS 안하고 그냥 정해진 답 출력 O(N)
그런데도 1900ms...
'''

from collections import deque

N, K = map(int, input().split())
startN = N
dest = K

nowLocation = deque([[startN, [startN]]])
isSearch = [0]*101001

def findLocation(dest, nowLocation:list, depth:int, memorize:list):
    while True:
        Location = nowLocation 
        now = Location.popleft()    # now : [value, [경로]]
        
        while type(now) == dict:
            depth = now['depth']
            now = Location.popleft()
            
        value = now[0]
        route = now[1]
        
        #print(f"dest: {dest}     now: {now}")
        # 탈출 조건
        if dest == now[0]:
            return now

        memorize[value] = 1
        Location.append({'depth':depth + 1})
        if (value-1) >= 0 and memorize[value-1] == 0:
            Location.append([value - 1, route + [value-1]])
        if (value+1) <= 101000 and memorize[value+1] == 0:
            Location.append([value + 1, route + [value+1]])
        if (value*2) <= 101000:
            if memorize[value*2] == 0:
                Location.append([value * 2, route + [value*2]])

        #print(f"현재: {now}        Depth: {depth}        Location: {Location}" )

if dest < startN:
    ans = []
    for i in range(startN, dest - 1, -1):
        ans.append(i)
    answer = [0, ans]        
else:        
    answer = findLocation(dest, nowLocation, 0, isSearch)
print(len(answer[1])-1)
[print(x, end=' ') for x in answer[1]]

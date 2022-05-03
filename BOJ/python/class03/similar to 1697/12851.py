# 12851번 숨바꼭질2
'''
1697 숨바꼭질1의 조건 + 가장 빠른 시간으로 찾는 방법의 수

BFS로 돌릴 때, 답이 나온 그 Depth를 전부 돌아보고 가짓수 구하기.

25분.
indexERR
*if문 순서에 주의하자. 
*재귀/while 문에서 탈출 조건 이전의 배열 접근에 주의하자.
'''

from collections import deque

N, K = map(int, input().split())
startN = N
dest = K

nowLocation = deque([startN])
isSearch = [0]*101001

def findLocation(dest, nowLocation:list, depth:int, memorize:list):
    while True:
        Location = nowLocation   
        now = Location.popleft()
    
        while type(now) == dict:
            depth = now['depth']
            now = Location.popleft()
        
        #print(f"dest: {dest}     now: {now}")
        if dest == now:  # 목적 값 찾았을 때.
            # 해당 Depth는 모두 탐색해서 가짓수 알아내야 함.
            cases = 1
            while True:
                #print(depth)
                #print(Location)
                if len(Location) == 0:
                    break
                elif type(now) == dict and now['depth'] != depth:
                    #print(now['depth'], type(now['depth']))
                    break
                else:
                    now = Location.popleft()
                    #print(Location)
                    '''if type(now) == dict:
                        print(now)
                        now = Location.popleft()
                    '''
                    #print(now)
                    if dest == now:
                        cases += 1
            
            return [depth, cases]

        memorize[now] = 1
        Location.append({'depth':depth + 1})
        if (now-1) >= 0 and memorize[now-1] == 0:
            Location.append(now - 1)
        if (now+1) <= 101000 and memorize[now+1] == 0:
            Location.append(now + 1)
        if (now*2) <= 101000:
            #print(now*2)
            if memorize[now*2] == 0:
                Location.append(now * 2)


        #print(f"현재: {now}        Depth: {depth}        Location: {Location}" )
        
        #if (depth == 5):
        #    return
    #finalDepth = findLocation(dest, Location, depth, memorize)
    #return finalDepth
    
answer = findLocation(dest, nowLocation, 0, isSearch)
[print(x) for x in answer]

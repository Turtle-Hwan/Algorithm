# 13549번 숨바꼭질3
'''
1697 숨바꼭질1과 다른 점: 2*X 위치로는 0초 걸림.

0-1 BFS??? 읭... https://justicehui.github.io/medium-algorithm/2018/08/30/01BFS/
<핵심>
가중치가 0인 간선과 1인 간선이 섞여있음.
어차피 BFS 큐에는 가중치(==depth)가 1 차이나는 두 무리밖에 안 들어있음.
즉 (n, v) 간선 가중치가 1이면 v를 큐 마지막에 넣고(원래대로), 가중치가 0이면 v를 큐 처음에 넣는다.


***
코드에서 단지 n*2일때 appendleft로만 바꾸니 맞네..
발상의 전환으로 간단히 0-1 섞인 BFS를 구현하는게 신기.
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
        if dest == now:
            return depth

        memorize[now] = 1
        Location.append({'depth':depth + 1})
        if (now-1) >= 0 and memorize[now-1] == 0:
            Location.append(now - 1)
        if (now+1) <= 101000 and memorize[now+1] == 0:
            Location.append(now + 1)
        if (now*2) <= 101000:
            #print(now*2)
            if memorize[now*2] == 0:
                Location.appendleft(now * 2)
                
        #print(f"현재: {now}        Depth: {depth}        Location: {Location}" )


answer = findLocation(dest, nowLocation, 0, isSearch)
print(answer)
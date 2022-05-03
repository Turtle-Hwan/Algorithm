# 1697번 숨바꼭질

'''
N, K 중 작은 값에서 시작.

+1, -1, *2  세 가지 경우가 있음.
트리 형태로 계속 분기하며 이어지도록.
BFS로 그 결과값을 탐색.

1 -> 100000 대략 2^16.xxx , 3번 분기니 3^17 = 1억2천만..


***
60분, 런타임 에러(재귀오류)

****
list pop(n) 은 O(n)
del list(n)도 O(n)
=> deque + deque.popleft() 이용!
****
in, not in 연산 O(n)
순회했는지, 탐색 했는지 여부 확인할 때는, 새로운 배열 만들고 index 이용해서 접근!!
a = [0]*10000, a[1] == 1 등.
****
pop from an empty deque가 발생할 상황
0 99999

120분.

수빈이가 동생을 찾아가는 것과 동생이 수빈이를 찾아가는 것은 다르다? 그러네...ㅡㄴㅡ
히히 맞아따. 1020ms 135mb...

'''

from collections import deque

N, K = map(int, input().split())

startN = N
dest = K

'''if N > K:
    startN = K
    dest = N
else:
    startN = N
    dest = K'''

nowLocation = deque([startN])
isSearch = [0]*101001

def findLocation(dest, nowLocation:list, depth:int, memorize:list):
    
    while True:
        #if dest in nowLocation:
        #    return depth
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
                Location.append(now * 2)


        #print(f"현재: {now}        Depth: {depth}        Location: {Location}" )
        
        #if (depth == 5):
        #    return
    #finalDepth = findLocation(dest, Location, depth, memorize)
    #return finalDepth
    
answer = findLocation(dest, nowLocation, 0, isSearch)
print(answer)
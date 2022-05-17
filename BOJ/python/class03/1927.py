#1927번 최소 힙
'''
힙 / 우선순위 큐  => python import heapq
우선순위 큐는 힙으로 구현하는 것이 효율적.

힙은 완전 이진 트리이므로 주로 배열로 구현함.
>>배열 인덱스 1이 root 노드.
부모의 인덱스 == 자식의 인덱스 // 2

30분. + 30분 ... heap 직접 구현하기 힘들다...
** heap pop 할 때 자식 두 개 비교해서 작은 것 올려줘야 함!!!
'''

'''
반례>
31
4
15
11
20
13
19
23
3
24
99
193
1
3
483
213
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

17
234
25
5
1
25
234
23345
235
0
0
0
0
0
0
0
0
0
>> 중복된 값 처리 안됨...  >> 부등호 -> 등호 문제

>> #자식 하나만 있는 경우 처리 안 됨.....!!!!!!!!!
'''

import sys

def popMin_heap():
    #print(heap)
    pop = heap[1]
    k = heap.pop()
    if len(heap) == 1:    # 기저조건
        return pop
    else:
        heap[1] = k

    n = 1    
    while True:
        if len(heap) <= n*2:    # 자식 없는 경우
            break
        elif len(heap) == n*2+1: #자식 하나만 있는 경우
            if heap[n] > heap[n*2]:
                heap[n], heap[n*2] = heap[n*2], heap[n]
                n *= 2 
            else:
                break
        else:    # 자식 두개 다 있는 경우 (n*2+1) < len(heap):
            if heap[n] > heap[n*2] and heap[n*2] <= heap[n*2+1]:
                heap[n], heap[n*2] = heap[n*2], heap[n]
                n *= 2
            elif heap[n] > heap[n*2+1] and heap[n*2] >= heap[n*2+1]:
                heap[n], heap[n*2+1] = heap[n*2+1], heap[n]
                n *= 2
                n += 1
            else:
                #print(heap[n])
                break
            #print(n)
    
    #노드 2개 남았을 때 따로 잡아줌...
    if len(heap) == 3 and heap[1] > heap[2]:
        heap[1], heap[2] = heap[2], heap[1]

    #print(heap)
    return pop


def insert_heap(x):
    heap.append(x)
    
    n = len(heap)-1
    while n >= 1:
        #print('dd', heap, heap[n], n)
        if heap[n] < heap[n//2]:
            heap[n], heap[n//2] = heap[n//2], heap[n]
        else:
            break
        n //= 2
    #print(heap)

        
N = int(input())
heap = [-1]
ans = []
for _ in range(0, N):
    x = int(sys.stdin.readline())
    if x == 0:    # 힙에서 가장 작은 값 출력 및 제거
        if len(heap) == 1:
            ans.append(0)
        else:
            ans.append(popMin_heap())
    else:    # 힙에 값 삽입
        insert_heap(x)

[print(x) for x in ans]
#11279번 최대 힙
'''
#1927번 최소 힙 참고
'''

import sys

def popMax_heap():
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
            if heap[n] < heap[n*2]:
                heap[n], heap[n*2] = heap[n*2], heap[n]
                n *= 2 
            else:
                break
        else:    # 자식 두개 다 있는 경우 (n*2+1) < len(heap):
            if heap[n] < heap[n*2] and heap[n*2] >= heap[n*2+1]:
                heap[n], heap[n*2] = heap[n*2], heap[n]
                n *= 2
            elif heap[n] < heap[n*2+1] and heap[n*2] <= heap[n*2+1]:
                heap[n], heap[n*2+1] = heap[n*2+1], heap[n]
                n *= 2
                n += 1
            else:
                break
            #print(n)
    
    #노드 2개 남았을 때 따로 잡아줌...
    if len(heap) == 3 and heap[1] < heap[2]:
        heap[1], heap[2] = heap[2], heap[1]
    #print(heap)
    return pop


def insert_heap(x):
    heap.append(x)
    
    n = len(heap)-1
    while n > 1:
        #print('dd', heap, heap[n], n)
        if heap[n] > heap[n//2]:
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
    if x == 0:    # 힙에서 가장 큰 값 출력 및 제거
        if len(heap) == 1:
            ans.append(0)
        else:
            ans.append(popMax_heap())
    else:    # 힙에 값 삽입
        insert_heap(x)

[print(x) for x in ans]
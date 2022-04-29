#10866번 덱

import sys
input = sys.stdin.readline

N = int(input())

deque = list()
answer = list()

for i in range(N):
    a = input().rstrip()

    if(a.find('push_front') != -1):
        deque.insert(0, a.lstrip('push_front '))

    elif(a.find('push_back') != -1):
        deque.append(a.lstrip('push_back '))
        
    elif(a == 'pop_front'):
        if(len(deque) == 0):
            answer.append(-1)
        else:
            answer.append(deque[0])
            del deque[0]

    elif(a == 'pop_back'):
        if(len(deque) == 0):
            answer.append(-1)
        else:
            answer.append(deque[-1])
            del deque[-1]

    elif(a == 'size'):
        answer.append(len(deque))
        
    elif(a == 'empty'):
        if(len(deque) == 0):
            answer.append(1)
        else:
            answer.append(0)

    elif(a == 'front'):
        if(len(deque) == 0):
            answer.append(-1)
        else:
            answer.append(deque[0])
            
    elif(a == 'back'):
        if(len(deque) == 0):
            answer.append(-1)
        else:
            answer.append(deque[-1])

[print(i) for i in answer]

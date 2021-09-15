#10845번 큐

import sys
input = sys.stdin.readline

N = int(input())

queue = list()
answer = list()

for i in range(N):
    a = input().rstrip()

    if(a.find('push') != -1):
        queue.append(a.lstrip('push '))
    elif(a == 'pop'):
        if(len(queue) == 0):
            answer.append(-1)
        else:
            answer.append(queue[0])
            del queue[0]
    elif(a == 'size'):
        answer.append(len(queue))
    elif(a == 'empty'):
        if(len(queue) == 0):
            answer.append(1)
        else:
            answer.append(0)
    elif(a == 'front'):
        if(len(queue) == 0):
            answer.append(-1)
        else:
            answer.append(queue[0])
    elif(a == 'back'):
        if(len(queue) == 0):
            answer.append(-1)
        else:
            answer.append(queue[len(queue)-1])

[print(i) for i in answer]

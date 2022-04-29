#10828번 스택

import sys
input = sys.stdin.readline

N = int(input())

order = list()
stack = list()
answer = list()

for i in range(N):
    order.append(input().rstrip())
    if(order[i].count('push') == 1):
        _, pushNum = order[i].split()
        stack.append(pushNum)
        
    elif(order[i] == 'pop'):
        if(len(stack) == 0):
            answer.append('-1')
        else:
            answer.append(stack.pop(-1))

    elif(order[i] == 'size'):
        answer.append(len(stack))

    elif(order[i] == 'empty'):
        if(len(stack) == 0):
            answer.append('1')
        else:
            answer.append('0')

    elif(order[i] == 'top'):
        if(len(stack) == 0):
            answer.append('-1')
        else:
            answer.append(stack[-1])


[print(x) for x in answer]


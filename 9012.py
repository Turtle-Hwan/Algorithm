#9012번 괄호

'''연속된 () 있으면 제거 -> 반복'''

import sys
input = sys.stdin.readline

T = int(input())

answer = list()

for i in range(T):
    PS = input()
    
    while(PS.find('()') != -1):
        PS = PS.replace('()', '')
        
    if(len(PS) == 1):
        answer.append('YES')
    else:
        answer.append('NO')

[print(i) for i in answer]

'''
    while(True):
        if(PS.find('()') != -1):
            PS = PS.replace('()', '')
        else:
            break
'''

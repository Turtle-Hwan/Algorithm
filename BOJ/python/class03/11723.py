#11723번 집합
'''
집합 자료형 구현..

dict으로 구현하는게 add, remove 시간복잡도가 더 좋을듯

시간초과.
in 연산 때문? >> dict 구현. // list로 해도 index 사용하면 똑같이 가능.

비트마스킹??!?!
And 연산 (&): 대응하는 두 비트가 모두 1이면 1 반환
1010 & 1111 = 1010
OR 연산 ( | ): 대응하는 두 비트 중 하나라도 1이면 1 반환
1010 & 1111 = 1111
Shift 연산 («,») : 비트를 왼쪽 또는 오른쪽으로 한칸씩 이동
0011 « 2 = 1100
1010 » 1 = 0101
XOR 연산 (^): 대응하는 두 비트가 다르면 1 같으면 0 반환
1010 ^ 1100 = 0110
Not 연산 (~) : 비트를 반전
~1111 = 0000
'''

def setS(command, x, S):
    if command == 'all':
        for i in range(1, 21):
            S[i] = 1
    elif command == 'empty':
        for i in range(1, 21):
            S[i] = 0
    elif command == 'add':
        S[x] = 1
    elif command == 'remove':
        S[x] = 0
    elif command == 'check':
        if S[x] == 1:
            print(1)
        else: 
            print(0)
    elif command == 'toggle':
        if S[x] == 1:
            S[x] = 0
        else:
            S[x] = 1
    #print(S)

import sys
input = sys.stdin.readline #().rstrip()

M = int(input())
S = dict()
setS('empty', -1, S)

for _ in range(0, M):   
    commandList = input().split()
    #print(commandList)
    if len(commandList) == 1:
        setS(commandList[0], -1, S)
    else:
        setS(commandList[0], int(commandList[1]), S)
        

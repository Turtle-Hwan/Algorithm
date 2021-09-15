#2947번 나무 조각

import sys
input = sys.stdin.readline

woods = list(map(int, input().split()))

while(True):
    if woods == [1, 2, 3, 4, 5]:
        break
    else:
        for x in range(len(woods)-1):
            if(woods[x] > woods [x+1]):
                woods.insert(x+1, woods.pop(x))
                [print(woods[i], end=' ') for i in range(len(woods))]
                print()

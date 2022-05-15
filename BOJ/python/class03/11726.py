#11726번, 2xn 타일링
'''
DP
종만북 252p / TILING2

"""
2개 묶음 == 2가지 / 나머지는 위치 방향 고정. 
=>> ??? 2개 묶어진 2x2 사각형들의 2xn 내부 배치 문제. (개수는 0~n//2)
하나 돌려놓고 다른 돌아간 묶음 배치
C 조합????
완탐 가능?
"""

종만북>>
맨 처음에 블럭 | 세로 하나 있는 경우 / 맨 처음에 = 가로 두 개 있는 경우 || 총 두 가지 경우의 합
세로 두 개 있는 경우는 세로 하나 -> 하나로 분리됨.
tiling(n) = tiling(n-1) + tiling(n-2)
'''
import sys
sys.setrecursionlimit(10**5)

def tiling(n):
    if n == 1:
        memory[1] = 1
        return 1
    elif n == 2:
        memory[2] = 2
        return 2
    elif memory[n] != 0:
        return memory[n]
    else:
        nex = tiling(n-1) + tiling(n-2)
        memory[n] = nex%10007
        return nex%10007

    
n = int(input())
memory = [0]*1001

print(tiling(n))


'''  반복문으로 완탐. (1부터 n까지 올라가면서 모두 배열에 집어넣기)
num = int(input())
arr = [0] * (num+1)

for n in range(1, num+1):
    if n == 1:
        arr[n] = 1
    elif n == 2:
        arr[n] = 2
    else:
        arr[n] = arr[n-1] + arr[n-2]
        if arr[n] >= 10007:
            arr[n] %= 10007

print(arr[num])
'''
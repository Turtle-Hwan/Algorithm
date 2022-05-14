# 1463 1로 만들기

# 3가지 다 해보면서 백트래킹? => 결국 1까지 도달해서 횟수를 구해야 하므로 백트래킹 불가능, DP 이용
'''
동적 계획법의 기본:
1. 완전 탐색을 설계
2. 중복된 부분 문제를 한 번만 계산하도록 메모이제이션 적용
'''

N = int(input())

answer = 0
memory = [1000001] * 1000001
memory[N] = 0
while N > 1:
    if N%3 == 0:
        if memory[int(N/3)] > memory[N] + 1:
            memory[int(N/3)] = memory[N] + 1
    if N%2 == 0:
        if memory[int(N/2)] > memory[N] + 1:
            memory[int(N/2)] = memory[N] + 1
    if memory[N-1] > memory[N] + 1:
        memory[N-1] = memory[N] + 1
    N = N - 1
    #print(N)

print(memory[1])

'''
n 입력
n -> tree1 tree2 tree3
memory 확인. 없으면
tree1 -> tree1 1 tree1 2 tree1 3

n에 대한 최솟값이면, 그때 거쳐간 모든 하위 노드들도 최솟값을 가진다.

tree 중 가장 빨리 1에 도달하는 경로 => answer = depth / 경로 저장.


10
9 5 === 1
8 3 ===2 / 4 === 2
7 4 ===3  [4] / 2 1 === 3 / 3
'''
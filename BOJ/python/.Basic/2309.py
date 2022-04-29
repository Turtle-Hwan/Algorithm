#2309번 일곱 난쟁이

from itertools import combinations

height = list()

for i in range(9):
    height.append(input())

combi = list(map(list, combinations(height, 7)))

for x in range(len(combi)):
    for y in range(len(combi[x])):
        combi[x][y] = int(combi[x][y])

for i in range(len(combi)):
    if(sum(combi[i]) == 100):
        answer = combi[i]
        break

answer.sort()

for i in range(len(answer)):
    print(answer[i])

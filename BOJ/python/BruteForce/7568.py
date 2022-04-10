# 7568 덩치

N = int(input())
inputList = list()

for i in range(0, N):
    x, y = map(int, input().split())
    inputList.append([x, y])

# N이 최대 50이므로, 일일히 비교해도 됨.
#print(inputList)

answer = list()

for i in range(0, N):
    x, y = inputList[i]
    rank = 1
    for j in range(0, N):
        a, b = inputList[j]
        if x<a and y<b:
            rank = rank + 1
    answer.append(rank)
    
[print(x, sep=' ') for x in answer]
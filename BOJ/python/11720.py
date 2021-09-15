#11720번 숫자의 합

N = int(input())

num = input()

totalSum = 0

for i in range(N):
    totalSum = totalSum + int(num[i])

print(totalSum)

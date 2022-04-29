#10950번 A+B - 3

testCase = int(input())

answer = list()

for i in range(testCase):
    A, B = input().split()
    answer.append(int(A) + int(B))

for i in range(testCase):
    print(answer[i])

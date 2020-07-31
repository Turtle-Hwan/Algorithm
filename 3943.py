#3943번 헤일스톤 수열
import sys

T = int(sys.stdin.readline())

testCase = list()

for i in range(T):
    testCase.append(int(sys.stdin.readline().rstrip()))

answer = list()
[answer.append(testCase[i]) for i in range(T)]

for i in range(T):
    n = testCase[i]
    while(True):
        if(n == 1):
            break
        else:
            if((n%2) == 0):
                n = n//2
            else:
                n = n*3 + 1
                if(answer[i] < n):
                    answer[i] = n


for i in range(T):
    print(answer[i])

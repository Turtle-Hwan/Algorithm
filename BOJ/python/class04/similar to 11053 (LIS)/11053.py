#11053번 가장 긴 증가하는 수열
'''
DP

일단 완탐. => O(n^2)
for i in range A[0] 부터 A[len(A)-1] 까지:
    for j in i~A[len(A)-1]:
        increase[i] = j부터 탐색하며 증가하는 수열
    

만약 A[3]이 A[0]부터 시작하는 증가하는 수열에 포함되어 있다면, 셀 필요 없을까? >> ㅇㅇ A[3]이 포함되려면 A[3] > A[0]임이 분명함
따라서 이미 탐색한 곳을 나타내는 visit[] 를 기억하면 DP로 시간 절약 가능.


###########
dp 개념에 관하여
https://www.acmicpc.net/board/view/61375
########
틀림. --- 1)
반례
6
1 2 8 2 4 8
ans 4

또틀림.. --- 2)
8
1 5 10 3 13 18 15 16
ans 6

10
1 5 10 3 13 18 19 15 16 17
ans 7

12
1 5 10 3 4 5 13 18 19 15 16 17
'''

"""
from collections import deque

N = input()
A = list(map(int, input().split()))
visit = [False]*len(A)
ans = []

for i in range(0, len(A)):
    if visit[i] == False:
        increaseL = deque()
        increaseL.append(A[i])
        visit[i] = True
        for j in range(i, -1, -1):    #1) 해결 위해. i가 0보다 클때, i보다 작은 부분 탐색해서 붙여주기
            if A[j] < increaseL[0]:
                increaseL.appendleft(A[j])
            elif len(increaseL) > 1 and A[j] < increaseL[1]:
                increaseL.popleft()
                increaseL.appendleft(A[j])
        for j in range(i, len(A)):
            if A[j] > increaseL[len(increaseL)-1]:
                increaseL.append(A[j])
                visit[j] = True
            elif A[j] > increaseL[len(increaseL)-2]:
                increaseL.pop()
                increaseL.append(A[j])
        ans.append(increaseL)
        print(i, ans, visit)

maxAnsLen = 1
for i in range(0, len(ans)):
    if len(ans[i]) > maxAnsLen:
        maxAnsLen = len(ans[i])
        
print(maxAnsLen)
"""

###### 그냥 다시 짜기..     // 위 코드는 일일히 비교했으나 특정 원소를 넣는 위치를 못 잡음. (이분 탐색으로 넣어야 한다!@!)
'''
위 방법: 하나씩 확인하며 넣기//

새로운 방법:
가짓수 모두 1로 초기화
맨 마지막부터 순회를 돌면서, 이전 원소보다 작으면 +1, 크면 작은 원소를 찾아가다가 그 원소 값 +1
완료하면 해당 값으로 시작하는 최장 증가 부분 수열의 개수가 저장됨.

참고:
https://chanhuiseok.github.io/posts/algo-49/
=> 여기서는 앞에서부터 순회 돌면서, 완료하면 해당 값으로 끝나는 최장 증가 부분 수열 개수가 저장.
'''

N = int(input())
A = list(map(int, input().split()))
LIS_len = [1]*N

for i in range(N-1, -1, -1):
    for j in range(i, N):
        #print(A[i], A[j])
        if A[i] < A[j]:
            LIS_len[i] = max(LIS_len[i], LIS_len[j] + 1)
            
print(max(LIS_len))
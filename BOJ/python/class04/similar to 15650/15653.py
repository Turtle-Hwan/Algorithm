#15653번 N과 M(5)
'''
서로 다른 N개 자연수 중 M개를 고른 수열을 모두 구함.
(이때, N개의 자연수가 각각 주어짐)


15650을 먼저 풂. 설명은 15650으로..

<<변경사항>>

'''

N, M = map(int, input().split())
NList = list(map(int, input().split()))
NList.sort()

visit = [False]*(N+1)
ans = []
mList = []

def combination(n, m, x): #n: 주어진 자연수 개수, 끝점, m: 골라야 하는 개수, 최대점, x: 고르기 시작하는 곳
    #print(ans, mList, visit)
    if len(mList) == m:
        ans.append(mList[:])
        return ans
    else:
        for i in range(1, n+1):
            if visit[i-1] == False:
                mList.append(NList[i-1])
                visit[i-1] = True
                combination(n, m, i+1)
                mList.pop()
                visit[i-1] = False
            
    
combination(N, M, 1)
[print(*i) for i in ans]

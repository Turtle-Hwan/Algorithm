#15649번 N과 M (1)
'''
N 중 중복 없이 M개 고르기 (순서 다른 건 다른 것으로)
N P M

15650을 먼저 풂. 설명은 15650으로..

15650 for range(x, n+1)에서 for range(1, n+1)
'''

N, M = map(int, input().split())
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
            if visit[i] == False:
                mList.append(i)
                visit[i] = True
                combination(n, m, i+1)
                mList.pop()
                visit[i] = False
    
combination(N, M, 1)
[print(*i) for i in ans]
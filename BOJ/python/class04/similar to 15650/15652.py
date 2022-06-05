#15652번 N과 M(4)
'''
N 중 중복 포함 M개 고르기 
but 고른 수열은 비내림차순!! (오름차순이거나 같거나)

15650을 먼저 풂. 설명은 15650으로..

<<변경사항>>
DFS 결과가 쌓이는 배열(mList) 이전 값과 비교하는 조건 추가.
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
            if len(mList) == 0 or mList[-1] <= i:
                mList.append(i)
                combination(n, m, i+1)
                mList.pop()
            
    
combination(N, M, 1)
[print(*i) for i in ans]

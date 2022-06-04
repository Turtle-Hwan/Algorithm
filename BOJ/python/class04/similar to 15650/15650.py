#15650번 N과 M (2)
'''
순열과 조합?
1~N 까지 중 중복 없이 M개 오름차순으로 고르기.

정렬은 보장되어 있으므로 1~N 중 중복 없이 M개 뽑는 가짓수 == N C M  조합. 


백트래킹.
1부터 해서 2 3 4
1 2 3 5 
1 2 3 6
1 2 4 5
이런 식으로 트리 만들어 나가면 될 듯
'''


'''
def a(시작점, 끝점N, ans 최대점M):
    if 답 length (== tree depth)가 주어진 M과 동일할 때.
        ans 삽입
        함수 종료 및 답 출력   =>>> list 얕은 복사되는거 주의!!
    else:
        for x~n:
            if 중복이 아닐 경우
                visit 처리
                mlist 삽입
                a(x+1) 다음 재귀
                ((다음 재귀에서 return 되었다면))mlist pop
                visit 미방문 처리
                
4 2
[1] [12] [1] [13] [1] [14] [1] [] [2] [23] [2] [24] [2] [] [3] [34] [3] [] [4] []
'''

N, M = map(int, input().split())
visit = [False]*(N+2)
ans = []
mList = []

def combination(n, m, x): #n: 주어진 자연수 개수, 끝점, m: 골라야 하는 개수, 최대점, x: 고르기 시작하는 곳
    #print(ans, mList, visit)
    if len(mList) == m:
        ans.append(mList[:])
        return ans
    else:
        for i in range(x, n+1):
            if visit[i] == False:
                mList.append(i)
                visit[i] = True
                combination(n, m, i+1)
                mList.pop()
                visit[i] = False
    
combination(N, M, 1)
[print(*i) for i in ans]
    

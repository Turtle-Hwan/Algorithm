#11722번 가장 긴 감소하는 부분 수열
'''
first: #11053
'''

#1 DP 이용
N = int(input())
A = list(map(int, input().split()))
LDS_len = [1]*N

for i in range(N-1, -1, -1):
    for j in range(i, N):
        #print(A[i], A[j])
        if A[i] > A[j]:
            LDS_len[i] = max(LDS_len[i], LDS_len[j] + 1)
            
print(max(LDS_len))






#11054번 가장 긴 바이토닉 부분 수열
'''
DP
DP memory에 해당 idx 값으로 끝나는 LIS, 해당idx로 시작하는 LDS 저장해놓고, 이 둘의 합이 가장 큰 것을 찾으면 될 듯.

아이디어.
LDS는 수열을 뒤집으면 증가수열 구하는 것과 같음.
'''

N = int(input())
A = list(map(int, input().split()))
LIS_len = [1]*N    #해당 index로 끝나는 LIS
LDS_len = [1]*N    #해당 index로 시작하는 LDS

for i in range(0, N):
    for j in range(0, i):
        #print(A[i], A[j])
        if A[i] > A[j]:
            LIS_len[i] = max(LIS_len[i], LIS_len[j] + 1)

for i in range(N-1, -1, -1):
    for j in range(i, N):
        if A[i] > A[j]:
            LDS_len[i] = max(LDS_len[i], LDS_len[j] + 1)
            
#print(LIS_len)
#ㄴprint(LDS_len)
LBS_len = [LIS_len[i] + LDS_len[i] - 1 for i in range(0, N)]
print(max(LBS_len))


            

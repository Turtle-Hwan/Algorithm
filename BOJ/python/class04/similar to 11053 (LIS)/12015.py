#12015번 가장 긴 증가하는 부분 수열 2 (입력 크기 증가)

'''
#1 DP
N = int(input())
A = list(map(int, input().split()))
LIS_len = [1]*N

for i in range(N-1, -1, -1):
    for j in range(i, N):
        #print(A[i], A[j])
        if A[i] < A[j]:
            LIS_len[i] = max(LIS_len[i], LIS_len[j] + 1)
            
print(max(LIS_len))
'''

#2 이분탐색 이용 증가하는 수열 구하기.
N = int(input())
A = list(map(int, input().split()))

def binarySearch_LIS(x, List):    # x를 List에 넣어야 할 index 반환.
    left = 0
    right = len(List)-1
    while True:
        m = (right - left) // 2 + left
        #print(left, right, m, x, List[m])
        if List[m] == x:    #같은 경우는 m번 인덱스를 바꿔야 함.
            return m 
        elif left > right:
            if left == right and List[left] > x:
                return m
            else:
                return m+1
        elif List[m] < x:
            left = m + 1
        elif x < List[m]:
            right = m - 1
 
LIS = [A[0]]
for i in A:
    idx = binarySearch_LIS(i, LIS)
    #print(idx, LIS, i)
    if idx < len(LIS):
        LIS[idx] = i
    else:
        LIS.append(i)

#print(LIS)
print(len(LIS))
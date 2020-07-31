#10250번 ACM호텔

'''
<입력>
T(testCase)
H W N
<출력>
N번째 손님에게 배정되는 방 번호

'N%H'+'N//H+1'

N%H == 0 일때
'''

T = int(input())

answer = list()

for i in range(T):
    H, W, N = map(int, input().split())

    if(N%H == 0):
        answer.append(H*100 + N//H)
    else:
        answer.append((N%H)*100 + N//H + 1)

for i in range(T):
    print(answer[i])

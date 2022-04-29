#11866번 요세푸스 문제 0

N, K = map(int, input().split())

a = list(range(1, N+1))

answer = list()


answer.append(a.pop(K-1))

nowIndex = K-1

for i in range(N-2):
    nowIndex = nowIndex+K-1
    if(nowIndex > len(a)-1):
        nowIndex = nowIndex%len(a)
    answer.append(a.pop(nowIndex))
        
if(len(a) == 1):
    answer.append(a[0])


print("<", end='')
[print(answer[i], ', ', sep='', end='') for i in range(N-1)]
print(answer[N-1], '>', sep='')

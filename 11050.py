#11050번 이항 계수 1

N, K = map(int, input().split())

a = 1
b = 1

for i in range(K):
    a *= N-i

for i in range(K):
    b *= K-i

print(int(a/b))

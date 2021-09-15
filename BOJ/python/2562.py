#2562번: 최댓값
'''
#리스트에 값 저장, max() 사용
n = list()

for i in range(9):
    n.append(int(input()))

maxnum = max(n)

print(maxnum)
print(n.index(maxnum)+1)
'''

n = list()

for i in range(9):
    n.append(int(input()))

#최댓값 찾기
maxnum = 0
for i in range(9):
    if(maxnum < n[i]):
        maxnum = n[i]


#출력
print(maxnum)
print(n.index(maxnum)+1)

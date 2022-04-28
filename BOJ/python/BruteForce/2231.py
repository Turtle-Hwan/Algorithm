# 2231번 분해합

# 1~10^6 분해합 다 구해놓고 찾아주기

N = int(input())

answerList = [0] * 1000000

def d(x):
    d = 0
    for n in range(0, 6):
        d = d + (x//pow(10, n))%10
    return d

for i in range(999999, 0, -1):
    #print(i)
    divSum = d(i)
    if divSum <= 1000000:
        answerList[i] = divSum

print(answerList[N])

#2460번 지능형 기차 2

getOn = list()
getOff = list()

for i in range(10):
    a, b = map(int, input().split())
    
    getOff.append(a)
    getOn.append(b)

inTrain = 0
answer = 0

for i in range(9):
    inTrain = inTrain + getOn[i]
    if(answer < inTrain):
        answer = inTrain
    inTrain = inTrain - getOff[i+1]
    
print(answer)

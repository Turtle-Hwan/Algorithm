#1259번 팰린드롬수

inputNum = list()

while True:
    a = input()
    if(a == '0'):
        break
    else:
        inputNum.append(a)

answer = list()

for i in range(len(inputNum)):
    if(inputNum[i][::-1] == inputNum[i]):
        answer.append('yes')
    else:
        answer.append('no')

for i in range(len(answer)):
    print(answer[i])

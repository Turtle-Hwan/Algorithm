#2161번 카드1

N = int(input())

card = list()
answer = list()

for i in range(N):
    card.append(i+1)

while(True):
    if(len(card) == 1):
        answer.append(card[0])
        break
    else:
        answer.append(card[0])
        card.pop(0)

        card.append(card[0])
        if(len(card) != 1):
            card.pop(0)
            

for i in range(N):
    print(answer[i], end=' ')

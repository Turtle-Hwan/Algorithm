#10952번 A+B - 5

answer = list()

while (True):
    A, B = input().split()
    
    if((int(A)==0) and (int(B)==0)):
        break
    else:
        answer.append(int(A) + int(B))


for i in range(len(answer)):
    print(answer[i])

#10951번 A+B - 4

answer = list()

while True:
    try:
        A, B = map(int, input().split())
        answer.append(A+B)

    except EOFError:
        break

for i in range(len(answer)):
    print(answer[i])

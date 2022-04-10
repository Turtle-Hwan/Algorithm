# 1065번 한수

N = int(input())

#print(a, b, c)

# N이 1~99이면 한수는 N개 // 그 외는 계산 // 1000 -> 4자리일 때 주의

if N < 100:
    print(N)
else:
    answer = 0
    for i in range(100, N+1):
        a = i//100
        b = i%100//10
        c = i%10
        
        if (a-b) == (b-c):
            answer = answer + 1
            
    print(answer + 99)

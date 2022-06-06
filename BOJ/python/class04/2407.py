#2407번 조합
'''
nCm  출력

n*n-1*...n-m+1           n!                 
-----------       =     ---------------
m!                        m! * (n-m)!
'''

N, M = map(int, input().split())
memory = [False]*101
memory[1] = 1
memory[2] = 2

def factorial(x): #팩토리얼 함수
    if memory[x] != False:
        return memory[x]
    else:
        memory[x] = x*factorial(x-1)
        return memory[x]


#print(factorial(N))
#print(factorial(M))
print(factorial(N)//factorial(M)//factorial(N-M))
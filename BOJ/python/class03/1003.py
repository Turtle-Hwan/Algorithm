#1003번 피보나치 함수
'''
30분.
DP

0, 1이 몇 번 호출되나 == fibonacci(0), fibonacci(1)의 호출 횟수
memorize 이용. +_원하는 호출 합도 memorize 해두기.
'''

#fibonacciMemo = [0] * 41
#ansSum = [{0: 0, 1: 0} for _ in range(0, 41)]    ==> 얕은 복사로 배열 이상해지는거 조심.

def fibonacci(n, fibonacciMemo, ansSum):
    #print(ansSum, n)
    if n == 0:
        ansSum[0][0] = 1
        return 0
    elif n == 1:
        fibonacciMemo[1] = 1
        ansSum[1][1] = 1
        return 1
    else:
        if fibonacciMemo[n] != 0:
            return fibonacciMemo[n]
        else:
            fibonacciMemo[n] = fibonacci(n-1, fibonacciMemo, ansSum) + fibonacci(n-2, fibonacciMemo, ansSum)
            #print(n, ansSum[n-1][0], ansSum[n-2][0])
            ansSum[n][0] = ansSum[n-1][0] + ansSum[n-2][0]
            ansSum[n][1] = ansSum[n-1][1] + ansSum[n-2][1]
            
            return fibonacciMemo[n]
        
    

T = int(input())

answer = []
for _ in range(0, T):
    N = int(input())
    
    fibonacciMemo = [0] * 41
    ansSum = [{0: 0, 1: 0} for _ in range(0, 41)]
    fibonacci(N, fibonacciMemo, ansSum)
    
    
    answer.append([ansSum[N][0], ansSum[N][1]])
   
for i in range(0, T):
    for x in answer[i]:
        print(x, end=' ')
    print()

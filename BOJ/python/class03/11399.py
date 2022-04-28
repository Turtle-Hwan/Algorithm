# 11399번 ATM

'''
각 사람(Pi)이 돈을 인출하는데 필요한 시간의 합의 최소.
가장 짧은 사람 순으로 정렬한 다음, 앞에서부터 더해 나간 것이 최소.

정렬 and 그리디

걸린 시간 : 10 min
* Pi가 좀 더 컸으면 합 구할 때 DP mamorize 쓰면 될 듯? 
'''

N = int(input())
Pi = list(map(int, input().split()))

Pi.sort()
minSum = 0
for i in range(0, len(Pi)+1):
    minSum += sum(Pi[0:i])
    #print(minSum)

print(minSum)
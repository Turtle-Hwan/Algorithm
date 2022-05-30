#1931번 회의실 배정
'''
그리디

먼저 끝나는걸 선택하면 된다.

증명..?

반례:
5
6 7
6 6
5 6
5 5
7 7
답 : 5
끝나는 시간도 고려하기!

6000ms.... 
개선점 : 
pop(0) 연산 대신 reverse 정렬해놓고 pop 하기. >> 4000ms  (pop 안하고 개수만 세기...?)

deque 쓰기?? >> 2차원 deque 정렬 방법 모르겠음. sprted 결과를 다시 deque에 넣어야 하나?

그래서 그냥 reverse 정렬 후 pop
'''
#from collections import deque

'''N = int(input())

meeting = list()#deque()
answer = 0
for _ in range(0, N):
    start, end = map(int, input().split())
    meeting.append([start, end])

meeting = sorted(meeting, key=lambda meeting: meeting[0])    
meeting = sorted(meeting, key=lambda meeting: meeting[1])    

while len(meeting) != 0:
    _, lastTime = meeting.pop(0)#popleft()
    answer += 1
    #print(lastTime)
    
    for i in range(0, len(meeting)):
        #print(meeting)
        if meeting[0][0] < lastTime:
            meeting.pop(0)#popleft()
        else:
            break
        
print(answer)'''


N = int(input())

meeting = list()#deque()
answer = 0
for _ in range(0, N):
    start, end = map(int, input().split())
    meeting.append([start, end])

meeting = sorted(meeting, key=lambda meeting:-meeting[0])    
meeting = sorted(meeting, key=lambda meeting:-meeting[1])    

while len(meeting) != 0:
    _, lastTime = meeting.pop()#popleft()
    answer += 1
    #print(lastTime)
    
    for i in range(0, len(meeting)):
        #print(meeting)
        if meeting[len(meeting)-1][0] < lastTime:
            meeting.pop()#popleft()
        else:
            break
        
print(answer)
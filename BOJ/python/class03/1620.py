#1620번 나는야 포켓몬 마스터 이다솜
'''
20~30분
dict으로 저장보다 list가 편한가?
>> but 시간초과....
>>>> 걍 키 값 한 번씩 바꿔서 둘다 dict으로 저장? >> 해결. 굳
'''

N, M = map(int, input().split())

encycNW = {}
encycWN = {}
for i in range(0, N):
    en = input()
    encycNW[str(i+1)] = en
    encycWN[en] = str(i+1)


ans = []
for _ in range(0, M):
    ask = input()
    if ask in encycWN.keys(): #영어일 때
        ans.append(encycWN[ask])    
    else: #숫자일 때
        ans.append(encycNW[ask])
    
[print(x) for x in ans]
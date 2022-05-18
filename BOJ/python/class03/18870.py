#18870번 좌표 압축
'''
<정렬> <좌표 압축>

좌표 압축>>
수 사이의 범위가 클 때 수의 값에 무관하게 좌표끼리 대소만 알고 싶을 때, 수의 범위를 줄이는 방법
> 임시 배열에 정렬된 상태 + 중복 제거 해서 넣었을 때 그 인덱스를 따로 저장하면 압축된다.


시간 초과// sort + for*array.index() => O(N^2) 
>> dict에 대소 순위(index) 담고, get으로 빼기 => O(N)
'''
N = int(input())
xCoor = list(map(int, input().split()))

sortA = list(set(xCoor))
sortA.sort()
dictA = dict()
for i in range(0, len(sortA)):
    dictA[sortA[i]] = i

for i in range(0, N):
    xCoor[i] = dictA.get(xCoor[i])
    
print(*xCoor)
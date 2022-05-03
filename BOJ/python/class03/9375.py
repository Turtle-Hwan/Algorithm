#9375 패션왕 신해빈

'''
입력받은 값 종류(눈장식, 머리장식, 상의, 하의, 신발)별로 각 배열에 집어넣기.

if 종류가 한가지일때:
    그 종류 배열 길이 출력.
else:
    각 종류 배열의 길이 모두 곱함.

상의 3개   1 2 3, 하의 4개   a b c d  , 눈장 ㄱ ㄴ 있을 때.
3 * 4 * 

4*3*2가지 + 3*4 + 4*2 + 3*2 + 3+4+2
==> 그냥 안 입는 경우까지 1 더해서 모두 곱한 후 마지막 1만 빼주자??

수학
자료 구조
조합론
해시를 사용한 집합과 맵  <<<???

dict? 
처음 입력받을 때 dict으로 받는게 어떻게 효율적일지?
pandas 느낌.
'''

TC = int(input())

ansList = []

for _ in range(0, TC):
    n = int(input())
    clouth = {}
    for _ in range(0, n):
        name, cType= input().split()
        if cType in clouth:
            clouth[f'{cType}'].append(name)
        else:
            clouth[f'{cType}'] = [name]
    
    ans = 1
    for i in clouth:
        ans *= len(clouth.get(i)) + 1
    ans -= 1
    ansList.append(ans)

[print(x) for x in ansList]
    
#for i in clouth:
#    print(clouth.get(i))
#print(clouth)

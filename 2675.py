#2675번 문자열 반복

testCase = int(input())

repeatNum = list()
repeatString = list()

for i in range(testCase):
    num, string = input().split()
    repeatNum.append(num)
    repeatString.append(string)

for i in range(testCase):
    for j in repeatString[i]:
        print(j*int(repeatNum[i]), end='')
    print()

'''
숫자와 문자열로 나눠진 입력값을 각각의 리스트에 집어넣어서
출력되도록 하는게 어려웠다.

입력을 split()으로 나눠서 변수에 저장한 후 리스트에 append()로 붙이는 것으로 해결.
'''

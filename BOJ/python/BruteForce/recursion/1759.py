#1759 암호 만들기

L, C = map(int, input().split())
charList = list(map(str, input().split()))

charList.sort()
#print(charList)

# aeiou 최소 1개, 최소 2개 자음.
# 사전순.

answerList = []

def password(list, n, a, b, word):
    global L
    #print(word)
    # 재귀 탈출 조건
    if len(list) == 0:
        if n == 0 and a <= 0 and b <= 0 and len(word) == L:
            answerList.append(word)
            
    elif n == 0 and a <= 0 and b <= 0 and len(word) == L:
        answerList.append(word)
    
    else:
        # list[0] 포함
        word = word + list[0]
        if list[0] in ['a', 'e', 'i', 'o', 'u']:
            password(list[1:], n-1, a-1, b, word)
        else:
            password(list[1:], n-1, a, b-1, word)

        # list[0] 미포함
        word = word[:-1]
        #print(word)
        password(list[1:], n, a, b, word)

            
password(charList, L, 1, 2, '')

#answerList.sort()
[print(x) for x in answerList]



''' 22:20~ 23:13
너무 힘들었다.
어려운 재귀. 안되는 과정을 찾기 위한 반복.

처음 잘못. 재귀로 이미 charList를 반복탐색 하는데 for문을 덧씌운 것.
두번째 잘못. list[0] 미포함하는 코드를 잘못 짠 것. 이전 word 삭제 필요했음. + 재귀 돌릴 때, n, a, b 그대로.
세번째 잘못. word를 외부에서 가져오려 했던 것. 그냥 지역 변수로 만들고 재귀에 넣었으면 됨.
네번째 잘못. list length가 0일 때 탈출 조건 필요. => 이것과 아래의 조건을 합칠 수 없나..?


++ 구름 IDE에서 파일별로 변화 추적할 수 있는 게 엄청 좋다.

++ 백준 서버 터져서 맞춰보지를 못함..

-- 반례)
3 5
a e o j k

로 global L 추가..
'''
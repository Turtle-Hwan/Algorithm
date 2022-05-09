# 17487번 타자 연습 (KAPC-A)
'''
'''

S = input()

leftHand = 'qwertyasdfgzxcvb'
rightHand = 'uiophjklnm'

SList = sorted(S, reverse=True)

leftClickNum = 0
rightClickNum = 0

for i in SList:    #기본 왼손/오른손인 경우 구분 + shift, space 키
    if i in leftHand:
        leftClickNum += 1
    elif i in rightHand:
        rightClickNum += 1
    elif i in leftHand.upper():
        leftClickNum += 1
        if leftClickNum <= rightClickNum:
            leftClickNum += 1
        else:
            rightClickNum += 1
    elif i in rightHand.upper():
        rightClickNum += 1
        if leftClickNum <= rightClickNum:
            leftClickNum += 1
        else:
            rightClickNum += 1
    elif i == ' ':
        if leftClickNum <= rightClickNum:
            leftClickNum += 1
        else:
            rightClickNum += 1
            
print(leftClickNum, rightClickNum)

        
        
        
    
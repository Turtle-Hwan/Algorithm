#8958번 OX퀴즈

testCase = int(input())

quizResult = list()

for i in range(testCase):
    quizResult.append(input())

for i in range(testCase):
    quizScore = 0
    quizScoreThis = 0
    
    for j in range(len(quizResult[i])):
        if(quizResult[i][j] == "O"):
            quizScoreThis = quizScoreThis + 1
        elif(quizResult[i][j] == "X"):
            quizScoreThis = 0
            
        quizScore = quizScore + quizScoreThis
        
    print(quizScore)

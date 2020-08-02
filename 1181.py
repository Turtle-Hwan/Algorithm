#1181번 단어 정렬

import sys
input = sys.stdin.readline

N = int(input())

words = dict()

for i in range(N):
    words.setdefault(input().rstrip())

wordsList = list(words)

wordsList2 = list()

for i in range(len(wordsList)):
    wordsList2.append([])
    wordsList2[i].append(wordsList[i])
    wordsList2[i].append(len(wordsList[i]))

a = sorted(wordsList2, key=lambda wordsList2: wordsList2[0])
b = sorted(a, key=lambda a: a[1])

[print(b[i][0]) for i in range(len(b))]


'''2차원 배열을 생성하고 정렬하는 방법을 생각해내지 못해 오래걸림.'''

# 알게 된 것 정리

*언어별 빠른 입출력 방법*
https://www.acmicpc.net/board/view/22716

*BOJ 채점 작동 원리*
https://www.acmicpc.net/blog/view/55

*자주 틀리는 요인*
https://www.acmicpc.net/blog/view/70

#### python
입력을 input()으로 받았을 때 시간초과
sys.stdin.readline()으로 받으면 더 빠르다.



파이썬3에서 재귀깊이 오류 주의
RecursionError: maximum recursion depth exceeded in comparison


###### 14405번
파이썬 내장함수 문자열.count 사용

###### 9012번
주의!
readline은 끝의 \n까지 읽어서 len(입력값)의 크기가 1 추가됨!

###### 1181번
파이썬 2차원 배열 정렬 2차원 배열 정렬 : 2차원 배열 정렬 sorted()

###### [1920번](https://github.com/Turtle-Hwan/Algorithm/commit/2a3b98e4ae837c76aeecd07eb5049a030050a46c#)
파이썬 자료형 기본 제공 함수 시간복잡도
https://blog.naver.com/kjhwan0802/222051208224

###### 10814번
print('3' > '20')
\>> True
숫자 크기로 정렬하고 싶다면 string 상태로 sort 하면 안된다.
sort는 오름차순으로 정렬함.
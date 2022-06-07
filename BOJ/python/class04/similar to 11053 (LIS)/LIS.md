# LIS (Longest Increasing Subsequence) 알고리즘
[LIS 알고리즘 참고 설명](https://chanhuiseok.github.io/posts/algo-49/)

1. DP 이용 O(n^2)
#11053번 참고.
앞에서 or 뒤에서 순회하면서 해당 숫자로 끝나는 or 시작하는 LIS 길이 저장.

2. 이분탐색 활용 O(nlogn)
기존 arr / 새로운 list 두고, 
기존 arr에서 값 하나씩 빼와서 새 list에 이분 탐색하여 앞에서부터 덮어씀.
마지막에 남는 list는 LIS


3. 스택 이용? (직접 생각)
O(n^2) ??
arr
stack
스택 만들어 두고, 
for i in arr:
    while True:
        if stack.last < i:
            stack.append(i)
            break
        else:
            stack.pop()
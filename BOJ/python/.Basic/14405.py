#14405번 피카츄

S = input()

if (S.count('pi')*2 + S.count('ka')*2 + S.count('chu')*3 == len(S)):
    print("YES")
else:
    print("NO")

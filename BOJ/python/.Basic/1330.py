#1330: 두 수 비교하기

A, B = input().split()

a = int(A)
b = int(B)

if(a<b):
    print("<")
elif(a>b):
    print(">")
elif(a==b):
    print("==")

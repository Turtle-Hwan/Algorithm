# 4673번 셀프 넘버

isSelfNumber = [1] * 10000

# 셀프 넘버 한 번씩 만들어봄.
for i in range(0, 10000):
    n = i + 1
    d = n + n%10 + n//10%10 + n//100%10 + n//1000%10 + n//10000%10
    
    if d <=10000:
        isSelfNumber[d-1] = 0

for i in range(0, 10000):
    if isSelfNumber[i] == 1:
        print(i+1)
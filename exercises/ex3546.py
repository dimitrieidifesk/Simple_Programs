n = int(input())
for i in range (100,1000):
    count = 0
    a = i
    while a > 0:
        count += a%10
        a //= 10
    if count == n:
        print (i)



